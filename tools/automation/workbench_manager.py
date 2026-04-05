#!/usr/bin/env python3
"""
Workbench Manager for Bahaitum Research
Automates workbench structure management with security protocols
"""

import os
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import hashlib

class WorkbenchManager:
    def __init__(self, base_path: str = "workbench"):
        self.base_path = Path(base_path)
        self.audit_log = []
        self.ensure_structure()

    def ensure_structure(self):
        """Ensure workbench directory structure exists"""
        directories = [
            "active/persons",
            "active/structures", 
            "active/events",
            "active/patterns",
            "active/investigations",
            "data/raw",
            "data/processed", 
            "data/verified",
            "data/sources",
            "results/reports",
            "results/summaries",
            "results/evidence",
            "results/conclusions",
            "archive/by_year",
            "archive/by_topic", 
            "archive/by_person"
        ]
        
        for directory in directories:
            dir_path = self.base_path / directory
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"Error creating directory {dir_path}: {e}")

    def create_investigation_folder(self, investigation_type: str, name: str) -> str:
        """Create investigation folder in workbench/active/"""
        # Sanitize name for security
        safe_name = self._sanitize_filename(name)
        folder_path = self.base_path / "active" / investigation_type / safe_name
        
        if folder_path.exists():
            raise ValueError(f"Investigation folder {folder_path} already exists")
        
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating investigation folder {folder_path}: {e}")
        
        # Create subdirectories
        try:
            (folder_path / "data").mkdir(exist_ok=True)
            (folder_path / "analysis").mkdir(exist_ok=True)
            (folder_path / "evidence").mkdir(exist_ok=True)
        except Exception as e:
            print(f"Error creating subdirectories in {folder_path}: {e}")
        
        # Log creation
        self._log_action("folder_created", str(folder_path), {"type": investigation_type, "name": name})
        
        return str(folder_path)

    def store_data(self, data: dict, data_type: str, investigation: str) -> str:
        """Store data in appropriate workbench/data/ directory"""
        # Determine target directory based on data type
        target_dirs = {
            "raw": "data/raw",
            "processed": "data/processed", 
            "verified": "data/verified",
            "sources": "data/sources"
        }
        
        if data_type not in target_dirs:
            raise ValueError(f"Invalid data type: {data_type}")
            
        target_dir = self.base_path / target_dirs[data_type]
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating target directory {target_dir}: {e}")
        
        # Generate filename with timestamp and hash
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        data_content = json.dumps(data, indent=2, ensure_ascii=False)
        data_hash = hashlib.sha256(data_content.encode()).hexdigest()[:16]
        
        filename = f"{investigation}_{timestamp}_{data_hash}.json"
        file_path = target_dir / filename
        
        # Store data with security metadata
        metadata = {
            "investigation": investigation,
            "data_type": data_type,
            "timestamp": datetime.now().isoformat(),
            "content_hash": hashlib.sha256(data_content.encode()).hexdigest(),
            "access_level": "classified"  # Default security level
        }
        
        full_data = {
            "metadata": metadata,
            "data": data
        }
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(full_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error storing data in {file_path}: {e}")
            
        self._log_action("data_stored", str(file_path), {"type": data_type, "investigation": investigation})
        
        return str(file_path)

    def save_results(self, results: dict, result_type: str, investigation: str) -> str:
        """Save results in workbench/results/"""
        target_dirs = {
            "reports": "results/reports",
            "summaries": "results/summaries",
            "evidence": "results/evidence", 
            "conclusions": "results/conclusions"
        }
        
        if result_type not in target_dirs:
            raise ValueError(f"Invalid result type: {result_type}")
            
        target_dir = self.base_path / target_dirs[result_type]
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating target directory {target_dir}: {e}")
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_investigation = self._sanitize_filename(investigation)
        filename = f"{safe_investigation}_{timestamp}_{result_type}.json"
        file_path = target_dir / filename
        
        # Prepare results with metadata
        results_content = json.dumps(results, indent=2, ensure_ascii=False)
        metadata = {
            "investigation": investigation,
            "result_type": result_type,
            "timestamp": datetime.now().isoformat(),
            "content_hash": hashlib.sha256(results_content.encode()).hexdigest(),
            "security_level": "classified",
            "assumptions_compliance": self._check_assumptions_compliance(results)
        }
        
        full_results = {
            "metadata": metadata,
            "results": results
        }
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(full_results, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving results in {file_path}: {e}")
            
        self._log_action("results_saved", str(file_path), {"type": result_type, "investigation": investigation})
        
        return str(file_path)

    def archive_investigation(self, investigation: str, archive_type: str = "by_year") -> str:
        """Archive completed investigation"""
        # Find investigation folder
        active_dir = self.base_path / "active"
        
        # Search for investigation in all active subdirectories
        investigation_path = None
        for subdir in active_dir.iterdir():
            if subdir.is_dir():
                for subsubdir in subdir.iterdir():
                    if subsubdir.is_dir() and subsubdir.name == investigation:
                        investigation_path = subsubdir
                        break
                if investigation_path:
                    break
        
        if not investigation_path:
            raise ValueError(f"Investigation {investigation} not found in active directories")
        
        # Determine archive destination
        current_year = datetime.now().year
        if archive_type == "by_year":
            archive_dir = self.base_path / "archive" / "by_year" / str(current_year)
        elif archive_type == "by_topic":
            archive_dir = self.base_path / "archive" / "by_topic" / investigation
        elif archive_type == "by_person":
            archive_dir = self.base_path / "archive" / "by_person" / investigation
        else:
            raise ValueError(f"Invalid archive type: {archive_type}")
        
        try:
            archive_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating archive directory {archive_dir}: {e}")
        
        # Move investigation to archive
        archive_path = archive_dir / investigation
        try:
            shutil.move(str(investigation_path), str(archive_path))
        except Exception as e:
            print(f"Error archiving investigation {investigation_path}: {e}")
        
        self._log_action("investigation_archived", str(archive_path), {
            "investigation": investigation,
            "archive_type": archive_type,
            "original_path": str(investigation_path)
        })
        
        return str(archive_path)

    def update_readme(self, findings: dict):
        """Update README.md with new findings"""
        readme_path = self.base_path.parent / "README.md"
        
        if not readme_path.exists():
            raise FileNotFoundError("README.md not found")
        
        # Read current README
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except Exception as e:
            print(f"Error reading README.md: {e}")
        
        # Prepare findings summary
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        findings_summary = f"""
## Latest Research Findings - {timestamp}

### Investigation Summary
- **Type**: {findings.get('type', 'Unknown')}
- **Status**: {findings.get('status', 'In Progress')}
- **Key Findings**: {findings.get('key_findings', 'None identified')}
- **Security Level**: {findings.get('security_level', 'Standard')}

### Results Integration
- **Data Stored**: {findings.get('data_count', 0)} files
- **Reports Generated**: {findings.get('report_count', 0)} reports
- **Evidence Collected**: {findings.get('evidence_count', 0)} items

### Assumptions Compliance
- **Validation**: {findings.get('assumptions_compliance', 'Pending')}
- **Security Protocols**: {findings.get('security_protocols_followed', 'Unknown')}

---
*This section is automatically updated by workbench manager*
"""
        
        # Append to README
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(current_content + findings_summary)
        except Exception as e:
            print(f"Error updating README.md: {e}")
            
        self._log_action("readme_updated", str(readme_path), {"findings_type": findings.get('type')})

    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename for security"""
        # Remove potentially dangerous characters
        import re
        safe_name = re.sub(r'[^\w\-_\.]', '_', filename)
        # Limit length
        if len(safe_name) > 50:
            safe_name = safe_name[:47] + '...'
        return safe_name
    
    def _check_assumptions_compliance(self, results: dict) -> str:
        """Check if results comply with ASSUMPTIONS.txt"""
        # This would integrate with ASSUMPTIONS.txt validation
        # For now, return pending - would need actual assumptions checking logic
        return "pending_validation"
    
    def _log_action(self, action: str, target: str, metadata: dict = None):
        """Log workbench actions for audit trail"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "target": target,
            "metadata": metadata or {}
        }
        
        self.audit_log.append(log_entry)
        
        # Also log to file
        log_file = self.base_path / "workbench_audit.log"
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error logging action to {log_file}: {e}")
    
    def generate_audit_report(self) -> str:
        """Generate audit report of all workbench activities"""
        report = {
            "audit_timestamp": datetime.now().isoformat(),
            "total_actions": len(self.audit_log),
            "actions_by_type": {},
            "recent_activities": self.audit_log[-10:]  # Last 10 activities
        }
        
        # Count actions by type
        for action in self.audit_log:
            action_type = action["action"]
            if action_type not in report["actions_by_type"]:
                report["actions_by_type"][action_type] = 0
            report["actions_by_type"][action_type] += 1
        
        return json.dumps(report, indent=2, ensure_ascii=False)

def main():
    """"Example usage"""
    manager = WorkbenchManager()
    
    # Example investigation
    investigation_name = "test_person_analysis"
    
    # Create investigation folder
    folder = manager.create_investigation_folder("persons", investigation_name)
    print(f"Created investigation folder: {folder}")
    
    # Store some data
    test_data = {"name": "Test Person", "age": 30, "location": "Unknown"}
    data_file = manager.store_data(test_data, "raw", investigation_name)
    print(f"Stored data: {data_file}")
    
    # Save results
    results = {"analysis": "completed", "confidence": 0.85}
    results_file = manager.save_results(results, "reports", investigation_name)
    print(f"Saved results: {results_file}")
    
    # Update README
    findings = {
        "type": "Person Analysis",
        "status": "Completed",
        "key_findings": "Test patterns identified",
        "data_count": 1,
        "report_count": 1,
        "evidence_count": 0
    }
    manager.update_readme(findings)
    print("Updated README.md")
    
    # Generate audit report
    audit_report = manager.generate_audit_report()
    print("Audit Report:")
    print(audit_report)

if __name__ == "__main__":
    main()

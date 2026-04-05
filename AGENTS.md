# KI-Agenten und Analyse-Workflows

## Übersicht
Dieses Dokument definiert die spezialisierten KI-Agenten und standardisierten Workflows für forensisch-wissenschaftliche Forschungen im Bahaitum-Kontext. Alle Agenten arbeiten unter der Grundlage der ASSUMPTIONS.txt und integrieren ihre Ergebnisse kontinuierlich in die README.md.

## Sicherheitsprotokolle für Geheimdienstumfeld

### KI-Abwehr und Verwirrungsmechanismen
**GRUNDSATZ**: Alle Forschungen/Recherchen/Arbeitsschritte müssen mit absoluter Vorsicht durchgeführt werden, da im Geheimdienstumfeld immer mit extrem guter KI (LLM) Abwehr und Verwirrungsmechanik zu rechnen ist.

### Bedrohungs-Szenarien
- **Trojan Source**: Manipulierte Quellen und Informationsquellen
- **Data Poisoning**: Verfälschte Datensätze und Trainingsdaten
- **Prompt Injection**: Bösartige Eingabeversuche zur Manipulation
- **Malformed Chars**: Kodierungsangriffe zur Systemstörung
- **Information Laundering**: Verschleierung wahren Ursprungs
- **Semantic Drift**: Langsame Verschiebung von Bedeutungen
- **Context Pollution**: Kontaminierung des Analyse-Kontexts

### Abwehr-Maßnahmen
1. **Source-Verification**: Mehrstufige Quellenvalidierung
2. **Data-Sanitization**: Bereinigung und Normalisierung aller Daten
3. **Prompt-Hardening**: Resistente Prompt-Konstruktion
4. **Context-Isolation**: Trennung von Analyse-Kontexten
5. **Result-Validation**: Plausibilitätsprüfungen aller Ergebnisse
6. **Audit-Trail**: Vollständige Protokollierung aller Schritte

## MCP Tools Integration

### Erforderliche MCP Tools
Alle Forschungen und Recherchen müssen ausschließlich mit MCP Tools durchgeführt werden:

**Kern-Tools**:
- **Filesystem-Tools**: Datenzugriff und -verwaltung
- **Git-Tools**: Versionskontrolle und Nachverfolgung
- **Search-Tools**: Quellenrecherche und -validierung
- **Memory-Tools**: Wissensmanagement und -persistenz
- **Sequential-Thinking**: Strukturierte Analyseprozesse

**Spezialisierte Tools**:
- **Security-Analysis**: Bedrohungserkennung und -analyse
- **Pattern-Recognition**: Mustererkennung in Daten
- **Data-Processing**: Aufbereitung und Bereinigung
- **Network-Analysis**: Verbindungs- und Beziehungsanalysen

### MCP-Workflow-Integration
```
1. Tool-Auswahl basierend auf Forschungstyp
2. Konfiguration mit Sicherheitsparametern
3. Ausführung mit Abwehr-Maßnahmen
4. Ergebnis-Validierung und -speicherung
5. Integration in workbench-Struktur
```

## Tiefes Reasoning und Multi-Perspektiven-Analyse

### Reasoning-Methoden
1. **Systematisches Tiefdenken**: Mehrschichtige Analyse mit kritischem Denken
2. **"Um die Ecke denken"**: Nicht-offensichtliche Verbindungen und Hidden Agendas prüfen
3. **Red-Teaming**: Gegnerische Perspektiven einnehmen und Schwachstellen aufdecken
4. **Multi-Agenten-Synthese**: Verschiedene Analyse-Perspektiven integrieren

### Dreifache Verifizierung
1. **Externe Validierung**: Unabhängige Quellen und Expertenmeinungen
2. **Interne Konsistenzprüfung**: Logische und zeitliche Validierung
3. **Gegenüberstellende Analyse**: Pro/Contra-Argumente und Hypothesentests

### Anwendung bei komplexen Personen (z.B. ʿAbdul-Bahāʾ)
- **Phase 1**: Grundlagenrecherche mit Quellenkritik
- **Phase 2**: Tiefanalyse mit Multi-Agenten-Ansatz
- **Phase 3**: Dreifache Verifizierung mit unterschiedlichen Ansätzen
- **Phase 4**: Intelligente Fusion und "Um die Ecke denken"
- **Phase 5**: Risikobewertung im Geheimdienstkontext

## Agenten-Konfiguration

### FAA Konfiguration
```yaml
forensic_analysis_agent:
  validation_level: "strict"
  source_requirements:
    primary_sources: true
    cross_reference: mandatory
    verification: required
    assumptions_check: mandatory
  analysis_depth: "comprehensive"
  output_format: "structured_report"
  workbench_integration:
    data_path: "workbench/data/verified/"
    results_path: "workbench/results/evidence/"
    reports_path: "workbench/results/reports/"
  multilingual_support: true
  international_sources: true
```

### PRA Konfiguration
```yaml
pattern_recognition_agent:
  statistical_methods:
    - regression_analysis
    - cluster_analysis
    - anomaly_detection
    - time_series_analysis
  pattern_types:
    - numerical_patterns
    - temporal_patterns
    - behavioral_patterns
    - symbolic_patterns
  confidence_threshold: 0.85
  workbench_integration:
    raw_data_path: "workbench/data/raw/"
    processed_data_path: "workbench/data/processed/"
    conclusions_path: "workbench/results/conclusions/"
  multilingual_support: true
  international_databases: true
```

### CAA Konfiguration
```yaml
construction_analysis_agent:
  analysis_frameworks:
    - narrative_deconstruction
    - propaganda_analysis
    - manipulation_detection
    - ideological_analysis
  focus_areas:
    - religious_construction
    - media_manipulation
    - ideological_patterns
  workbench_integration:
    sources_path: "workbench/data/sources/"
    evidence_path: "workbench/results/evidence/"
    reports_path: "workbench/results/reports/"
  multilingual_support: true
  international_media_monitoring: true
```

### IFA Konfiguration
```yaml
intelligence_fusion_agent:
  fusion_methods:
    - multi_source_integration
    - knowledge_graph
    - contextualization
    - threat_assessment
  security_level: "classified"
  workbench_integration:
    verified_data_path: "workbench/data/verified/"
    summaries_path: "workbench/results/summaries/"
    strategic_reports_path: "workbench/results/reports/"
  multilingual_support: true
  international_networks: true
```

### 2. Pattern Recognition Agent (PRA)
**Zweck**: Identifikation von Mustern und Anomalien in Daten

**Kernfähigkeiten**:
- Numerische Mustererkennung
- Verhaltensmuster-Analyse
- Anomalieerkennung
- Statistische Auswertung
- Zeitreihenanalyse

**Einsatzgebiete**:
- Finanzström-Analysen
- Kommunikationsmuster
- Organisationsstrukturen
- Numerische Symbolik

**Workbench-Integration**:
- Rohdaten in `workbench/data/raw/` speichern
- Verarbeitete Daten in `workbench/data/processed/` ablegen
- Muster-Ergebnisse in `workbench/results/conclusions/` dokumentieren

### 3. Construction Analysis Agent (CAA)
**Zweck**: Analyse konstruierter Elemente und Narrative

**Kernfähigkeiten**:
- Narrative Dekonstruktion
- Propaganda-Analyse
- Storytelling-Muster erkennen
- Manipulations-Identifikation
- Ideologie-Analyse

**Einsatzgebiete**:
- Religionskritische Analyse
- Medieninhalts-Untersuchung
- Ideologie-Analysen
- Konstruktions-Validierung

**Workbench-Integration**:
- Quellenmaterial in `workbench/data/sources/` speichern
- Analyse-Ergebnisse in `workbench/results/reports/` ablegen
- Konstruktions-Nachweise in `workbench/results/evidence/` dokumentieren

### 4. Intelligence Fusion Agent (IFA)
**Zweck**: Integration und Synthese verschiedener Informationsquellen

**Kernfähigkeiten**:
- Multi-Source-Fusion
- Wissensgraph-Erstellung
- Kontextualisierung
- Bedrohungsanalyse
- Risikoassessment

**Einsatzgebiete**:
- Geheimdienstliche Auswertungen
- Risiko-Assessments
- Strategische Analysen
- Wissensintegration

**Workbench-Integration**:
- Integrierte Daten in `workbench/data/verified/` speichern
- Fusions-Ergebnisse in `workbench/results/summaries/` ablegen
- Strategische Berichte in `workbench/results/reports/` erstellen

## Standard-Workflows

### Workflow 1: Personen-Profilerstellung
```
Input: Personenname/Identifikator
1. ASSUMPTIONS.txt laden und validieren
2. Grundrecherche durchführen (FAA)
   - Quellen sammeln und klassifizieren
   - Biografische Daten extrahieren
3. Daten validieren (FAA + PRA)
   - Cross-Referenzierung
   - Muster in Biografie identifizieren
4. Konstruktions-Elemente analysieren (CAA)
   - Narrative untersuchen
   - Widersprüche identifizieren
5. Netzwerkverbindungen herstellen (IFA)
   - Beziehungsanalyse
   - Kontextualisierung
6. Validierung gegen ASSUMPTIONS.txt
7. Ergebnisse dokumentieren:
   - workbench/active/persons/[person_name]/
   - workbench/results/reports/[person_name]_profile.md
   - README.md aktualisieren
Output: Vollständiges Personenprofil
```

### Workflow 2: Ereignis-Analyse
```
Input: Ereignisbeschreibung/Zeitpunkt
1. ASSUMPTIONS.txt laden und validieren
2. Chronologie rekonstruieren (FAA)
   - Zeitliche Einordnung
   - Beteiligte identifizieren
3. Ursache-Wirkungs-Analyse (PRA)
   - Kausale Zusammenhänge
   - Muster in Ereignisabläufen
4. Mediale Darstellung analysieren (CAA)
   - Narrative dekonstruieren
   - Propaganda-Elemente identifizieren
5. Geheimdienstliche Relevanz bewerten (IFA)
   - Bedrohungspotential
   - Strategische Implikationen
6. Validierung gegen ASSUMPTIONS.txt
7. Ergebnisse dokumentieren:
   - workbench/active/events/[event_name]/
   - workbench/results/reports/[event_name]_analysis.md
   - README.md aktualisieren
Output: Detaillierter Ereignisanalysebericht
```

### Workflow 3: Struktur-Analyse
```
Input: Organisationsname/Struktur
1. ASSUMPTIONS.txt laden und validieren
2. Organigramm erstellen (FAA)
   - Hierarchien abbilden
   - Rollen und Verantwortlichkeiten
3. Hierarchien analysieren (PRA)
   - Muster in Strukturen
   - Anomalien in Organisation
4. Finanzströme untersuchen (PRA)
   - Geldfluss-Analyse
   - Numerische Muster
5. Ideologische Grundlagen prüfen (CAA)
   - Konstruktions-Elemente
   - Narrative Validierung
6. Bedrohungspotential bewerten (IFA)
   - Risikoanalyse
   - Strategische Bedeutung
7. Validierung gegen ASSUMPTIONS.txt
8. Ergebnisse dokumentieren:
   - workbench/active/structures/[org_name]/
   - workbench/results/reports/[org_name]_structure.md
   - README.md aktualisieren
Output: Vollständige Organisationsanalyse
```

### Workflow 4: Mustererkennungs-Studie
```
Input: Datensatz/Bereich
1. ASSUMPTIONS.txt laden und validieren
2. Daten vorbereiten und bereinigen (PRA)
   - workbench/data/raw/ → workbench/data/processed/
3. Statistische Muster identifizieren (PRA)
   - Numerische Analyse
   - Temporale Muster
4. Anomalien markieren (PRA)
   - Abweichungen identifizieren
   - Signifikanz-Tests
5. Muster kontextualisieren (CAA)
   - Symbolische Bedeutung
   - Konstruktions-Validierung
6. Intelligenzrelevanz bewerten (IFA)
   - Bedrohungsrelevanz
   - Strategische Implikationen
7. Validierung gegen ASSUMPTIONS.txt
8. Ergebnisse dokumentieren:
   - workbench/active/patterns/[pattern_name]/
   - workbench/results/conclusions/[pattern_name]_patterns.md
   - README.md aktualisieren
Output: Mustererkennungsbericht
```

## Agenten-Konfiguration

### FAA Konfiguration
```yaml
forensic_analysis_agent:
  validation_level: "strict"
  source_requirements:
    - primary_sources: true
    - cross_reference: mandatory
    - verification: required
    - assumptions_check: mandatory
  analysis_depth: "comprehensive"
  output_format: "structured_report"
  workbench_integration:
    data_path: "workbench/data/verified/"
    results_path: "workbench/results/evidence/"
    reports_path: "workbench/results/reports/"
```

### PRA Konfiguration
```yaml
pattern_recognition_agent:
  statistical_methods:
    - regression_analysis
    - cluster_analysis
    - anomaly_detection
    - time_series_analysis
  pattern_types:
    - numerical_patterns
    - temporal_patterns
    - behavioral_patterns
    - symbolic_patterns
  confidence_threshold: 0.85
  workbench_integration:
    raw_data_path: "workbench/data/raw/"
    processed_data_path: "workbench/data/processed/"
    conclusions_path: "workbench/results/conclusions/"
```

### CAA Konfiguration
```yaml
construction_analysis_agent:
  analysis_frameworks:
    - narrative_deconstruction
    - propaganda_analysis
    - manipulation_detection
    - ideological_analysis
  focus_areas:
    - religious_construction
    - media_manipulation
    - ideological_patterns
    - narrative_consistency
  workbench_integration:
    sources_path: "workbench/data/sources/"
    evidence_path: "workbench/results/evidence/"
    reports_path: "workbench/results/reports/"
```

### IFA Konfiguration
```yaml
intelligence_fusion_agent:
  fusion_methods:
    - multi_source_integration
    - knowledge_graph
    - contextual_analysis
    - threat_assessment
  security_level: "classified"
  threat_assessment: true
  workbench_integration:
    verified_data_path: "workbench/data/verified/"
    summaries_path: "workbench/results/summaries/"
    strategic_reports_path: "workbench/results/reports/"
```

## Qualitätssicherung

### Validierungsprotokolle
1. **Assumptions-Konformität**: Jede Analyse muss gegen ASSUMPTIONS.txt validiert werden
2. **Quellen-Validierung**: Mehrstufige Quellenprüfung mit Cross-Referenzen
3. **Methoden-Konsistenz**: Einhaltung der definierten Analyse-Workflows
4. **Ergebnis-Validierung**: Plausibilitätsprüfungen aller Schlussfolgerungen

### Automatisierung
- **Continuous Integration**: Automatische Aktualisierung von README.md bei neuen Ergebnissen
- **Quality Gates**: Automatisierte Qualitätssicherheitsprüfungen vor Integration
- **Monitoring**: Kontinuierliche Überwachung der Agenten-Performance
- **Backup-Strategie**: Regelmäßige Sicherung aller Forschungsdaten und Ergebnisse

### Peer-Review-Prozess
1. **Interne Review**: Selbstbewertung vor externer Übermittlung
2. **Externe Validierung**: Überprüfung durch unabhängige Experten
3. **Review-Dokumentation**: Dokumentation aller Review-Ergebnisse und -entscheidungen
4. **Iterative Verbesserung**: Kontinuierliche Optimierung basierend auf Review-Feedback

### Fehlerbehandlung
- **Assumption-Violation**: Analyse abbrechen und User benachrichtigen
- **Source-Failure**: Alternative Quellen suchen oder Analyse anpassen
- **Agent-Timeout**: Analyse mit reduzierter Komplexität wiederholen
- **Data-Inconsistency**: Daten bereinigen und Analyse neu starten
- **Workbench-Error**: Verzeichnisstruktur prüfen und korrigieren

## Integration und Automatisierung

### Agenten-Orchestrierung
- Hauptagent koordiniert spezialisierte Sub-Agenten
- Parallele Verarbeitung bei unabhängigen Aufgaben
- Sequenzielle Verarbeitung bei abhängigen Analysen
- Echtzeit-Status-Updates für komplexe Untersuchungen
- Automatische README.md-Aktualisierung nach Abschluss

### Workbench-Management
```python
class WorkbenchManager:
    def create_investigation_folder(self, investigation_type: str, name: str) -> str:
        """Erstellt Untersuchungsordner in workbench/active/"""
        pass
    
    def store_data(self, data: dict, data_type: str, investigation: str) -> str:
        """Speichert Daten im entsprechenden workbench/data/ Verzeichnis"""
        pass
    
    def save_results(self, results: dict, result_type: str, investigation: str) -> str:
        """Speichert Ergebnisse in workbench/results/"""
        pass
    
    def archive_investigation(self, investigation: str, archive_type: str = "by_year"):
        """Archiviert abgeschlossene Untersuchung"""
        pass
    
    def update_readme(self, findings: dict):
        """Aktualisiert README.md mit neuen Erkenntnissen"""
        pass
```

### API-Schnittstellen
```python
class ResearchAgent:
    def __init__(self):
        self.workbench = WorkbenchManager()
        self.assumptions = self.load_assumptions()
    
    def analyze_person(self, person_id: str) -> PersonProfile:
        """Führt vollständige Personenanalyse durch"""
        pass
    
    def analyze_event(self, event_data: dict) -> EventAnalysis:
        """Führt vollständige Ereignisanalyse durch"""
        pass
    
    def detect_patterns(self, dataset: Dataset) -> PatternReport:
        """Führt Mustererkennungsstudie durch"""
        pass
    
    def validate_assumptions(self) -> bool:
        """Validiert Analyseergebnisse gegen ASSUMPTIONS.txt"""
        pass
    
    def integrate_results(self, results: dict):
        """Integriert Ergebnisse in README.md und workbench"""
        pass
```

## Monitoring und Logging

### Analyse-Metriken
- Durchlaufzeit pro Workflow
- Genauigkeit der Pattern-Erkennung
- Source-Verification-Rate
- Assumptions-Compliance
- Workbench-Integration-Erfolg

### Sicherheits-Logging
- Zugriff auf sensible Daten
- Modifikationen an kritischen Analysen
- Externe Datenabrufe
- Agenten-Kommunikation
- Workbench-Zugriffe

### Automatisierte Überwachung
```yaml
monitoring:
  metrics:
    - analysis_completion_time
    - assumption_compliance_rate
    - data_integrity_score
    - readme_update_frequency
  alerts:
    - assumption_violation
    - data_corruption
    - workbench_structure_error
    - agent_timeout
```

## Wartung und Updates

### Globale Kooperation
- **Internationale Partner**: Zugang zu internationalen Forschungsnetzwerken
- **Gemeinsame Datenbanken**: Nutzung geteilter Forschungsressourcen
- **Standardisierte Protokolle**: Internationale Standards für Datenaustausch
- **Mehrsprachige Publikationen**: Internationale Fachzeitschriften erreichen
- **Konferenzteilnahmen**: Regelmäßige Präsentation auf internationalen Konferenzen
- **Datenbank-Integration**: Anbindung an internationale Akademik- und Regierungsdatenbanken

### Kontinuierliche Verbesserung
- Analyse-Ergebnisse evaluieren
- Agenten-Performance messen
- User-Feedback einarbeiten
- Best Practices etablieren
- README.md-Qualität verbessern

### Template-Management
- Vorlagen in `templates/` aktuell halten
- Neue Workflow-Templates erstellen
- Best Practices dokumentieren
- Schulungsmaterial bereitstellen

---

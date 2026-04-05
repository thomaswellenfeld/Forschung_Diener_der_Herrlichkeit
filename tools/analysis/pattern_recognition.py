#!/usr/bin/env python3
"""
Pattern Recognition Tool for Bahaitum Research
Identifies patterns in data with security-aware analysis
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import json

class PatternRecognizer:
    def __init__(self):
        self.patterns_found = []
        self.anomalies = []
        self.security_alerts = []

    def analyze_numerical_patterns(self, data: List[float]) -> Dict:
        """Analyze numerical patterns for potential manipulation"""
        result = {
            'pattern_type': 'numerical',
            'timestamp': datetime.now().isoformat(),
            'patterns': [],
            'anomalies': [],
            'security_flags': [],
            'confidence': 0.0
        }
        
        try:
            data_array = np.array(data)
            
            # Statistical analysis
            mean = np.mean(data_array)
            std = np.std(data_array)
            
            # Pattern detection
            patterns = []
            
            # Check for arithmetic sequences
            if self._is_arithmetic_sequence(data_array):
                patterns.append({
                    'type': 'arithmetic_sequence',
                    'description': 'Data follows arithmetic progression',
                    'confidence': 0.8
                })
            
            # Check for geometric sequences
            if self._is_geometric_sequence(data_array):
                patterns.append({
                    'type': 'geometric_sequence',
                    'description': 'Data follows geometric progression',
                    'confidence': 0.7
                })
            
            # Check for repeating patterns
            if self._has_repeating_pattern(data_array):
                patterns.append({
                    'type': 'repeating_pattern',
                    'description': 'Data contains repeating elements',
                    'confidence': 0.9
                })
            
            # Anomaly detection
            anomalies = []
            z_scores = np.abs((data_array - mean) / std)
            
            for i, z_score in enumerate(z_scores):
                if abs(z_score) > 2.5:  # Threshold for anomaly
                    anomalies.append({
                        'index': i,
                        'value': float(data_array[i]),
                        'z_score': float(z_score),
                        'type': 'statistical_outlier'
                    })
            
            # Security checks
            security_flags = []
            if self._indicates_data_poisoning(data_array):
                security_flags.append('potential_data_poisoning')
            
            if self._shows_semantic_drift(data_array):
                security_flags.append('semantic_drift_detected')
            
            result['patterns'] = patterns
            result['anomalies'] = anomalies
            result['security_flags'] = security_flags
            result['confidence'] = self._calculate_overall_confidence(patterns, anomalies)
            
        except Exception as e:
            result['security_flags'].append(f'analysis_error_{str(e)}')
            
        return result
    
    def analyze_temporal_patterns(self, time_series_data: List[Tuple]) -> Dict:
        """Analyze temporal patterns in time series data"""
        result = {
            'pattern_type': 'temporal',
            'timestamp': datetime.now().isoformat(),
            'patterns': [],
            'anomalies': [],
            'security_flags': [],
            'confidence': 0.0
        }
        
        try:
            # Extract timestamps and values
            timestamps = [item[0] for item in time_series_data]
            values = [item[1] for item in time_series_data]
            
            # Convert to pandas for time series analysis
            df = pd.DataFrame({'timestamp': timestamps, 'value': values})
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df.sort_values('timestamp')
            
            patterns = []
            
            # Check for periodicity
            if len(values) > 10:
                # Simple periodicity check
                autocorr = [self._autocorrelation(values, lag) for lag in range(1, min(10, len(values)//2))]
                max_corr_lag = np.argmax(autocorr) + 1 if autocorr else 0
                
                if max_corr_lag > 0:
                    patterns.append({
                        'type': 'periodic_pattern',
                        'period': max_corr_lag,
                        'description': f'Pattern repeats every {max_corr_lag} periods',
                        'confidence': 0.6
                    })
            
            # Check for trend patterns
            if len(values) > 5:
                trend_slope = self._calculate_trend(values)
                if abs(trend_slope) > 0.1:
                    patterns.append({
                        'type': 'trend_pattern',
                        'slope': trend_slope,
                        'description': 'Data shows clear trend',
                        'confidence': 0.7
                    })
            
            # Anomaly detection in temporal data
            anomalies = []
            if len(values) > 5:
                moving_avg = pd.Series(values).rolling(window=3).mean().tolist()
                residuals = [values[i] - moving_avg[i] for i in range(len(values)) if not np.isnan(moving_avg[i])]
                
                for i, residual in enumerate(residuals):
                    if abs(residual) > 2 * np.std(residuals):
                        anomalies.append({
                            'timestamp': timestamps[i],
                            'value': values[i],
                            'residual': residual,
                            'type': 'temporal_anomaly'
                        })
            
            # Security checks for temporal data
            security_flags = []
            if self._indicates_temporal_manipulation(timestamps, values):
                security_flags.append('temporal_manipulation_indicators')
            
            result['patterns'] = patterns
            result['anomalies'] = anomalies
            result['security_flags'] = security_flags
            result['confidence'] = self._calculate_overall_confidence(patterns, anomalies)
            
        except Exception as e:
            result['security_flags'].append(f'temporal_analysis_error_{str(e)}')
            
        return result

    def _is_arithmetic_sequence(self, data: np.ndarray) -> bool:
        """Check if data follows arithmetic progression"""
        if len(data) < 3:
            return False
        
        differences = np.diff(data)
        return np.allclose(differences, differences[0], rtol=0.1)
    
    def _is_geometric_sequence(self, data: np.ndarray) -> bool:
        """Check if data follows geometric progression"""
        if len(data) < 3:
            return False
        
        ratios = data[1:] / data[:-1]
        return np.allclose(ratios, ratios[0], rtol=0.1)
    
    def _has_repeating_pattern(self, data: np.ndarray) -> bool:
        """Check for repeating patterns in data"""
        if len(data) < 6:
            return False
        
        # Check for simple repetition
        half_len = len(data) // 2
        first_half = data[:half_len]
        second_half = data[half_len:half_len*2]
        
        return np.array_equal(first_half, second_half)
    
    def _indicates_data_poisoning(self, data: np.ndarray) -> bool:
        """Check for indicators of data poisoning"""
        # Simplified checks - would need more sophisticated analysis
        if len(data) < 10:
            return False
        
        # Check for unrealistic outliers that could indicate poisoning
        q75, q25 = np.percentile(data, [75, 25])
        iqr = q75 - q25
        
        # Check for extreme outliers
        extreme_outliers = np.sum((data > q75 + 3*iqr) | (data < q25 - 3*iqr))
        
        return extreme_outliers > len(data) * 0.1
    
    def _shows_semantic_drift(self, data: np.ndarray) -> bool:
        """Check for semantic drift indicators"""
        # Simplified semantic drift detection
        if len(data) < 20:
            return False
        
        # Compare first half to second half
        mid = len(data) // 2
        first_half = data[:mid]
        second_half = data[mid:]
        
        # Check for significant distribution change
        first_mean, second_mean = np.mean(first_half), np.mean(second_half)
        first_std, second_std = np.std(first_half), np.std(second_half)
        
        mean_diff = abs(first_mean - second_mean)
        std_ratio = second_std / first_std if first_std > 0 else 1
        
        return mean_diff > 2 * first_std or std_ratio > 2 or std_ratio < 0.5
    
    def _autocorrelation(self, data: List[float], lag: int) -> float:
        """Calculate autocorrelation at given lag"""
        if lag >= len(data):
            return 0
        
        n = len(data)
        data_array = np.array(data)
        
        # Calculate correlation between original and lagged series
        original = data_array[:-lag] if lag > 0 else data_array
        lagged = data_array[lag:] if lag > 0 else data_array
        
        if len(original) != len(lagged):
            return 0
        
        correlation = np.corrcoef(original, lagged)[0, 1]
        return correlation if not np.isnan(correlation) else 0
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend slope using linear regression"""
        if len(values) < 3:
            return 0
        
        x = np.arange(len(values))
        y = np.array(values)
        
        # Simple linear regression
        slope = np.polyfit(x, y, 1)[0]
        return slope
    
    def _indicates_temporal_manipulation(self, timestamps: List, values: List[float]) -> bool:
        """Check for temporal manipulation indicators"""
        if len(timestamps) < 5:
            return False
        
        # Check for irregular time gaps
        time_diffs = np.diff(timestamps)
        irregular_gaps = np.sum(time_diffs > np.mean(time_diffs) + 2*np.std(time_diffs))
        
        # Check for value patterns that don't match time patterns
        value_changes = np.diff(values)
        synchronized_changes = np.allclose(value_changes, time_diffs[:len(value_changes)], rtol=0.5)
        
        return irregular_gaps > 0 or not synchronized_changes
    
    def _calculate_overall_confidence(self, patterns: List[Dict], anomalies: List[Dict]) -> float:
        """Calculate overall confidence in analysis"""
        if not patterns and not anomalies:
            return 0.0
        
        pattern_confidence = np.mean([p.get('confidence', 0) for p in patterns]) if patterns else 0.5
        anomaly_count_factor = min(len(anomalies) / 10, 1.0)  # More anomalies = higher confidence
        
        return min(pattern_confidence + anomaly_count_factor, 1.0)

    def generate_report(self, results: List[Dict]) -> str:
        report = "Pattern Recognition Report:\n"
        for result in results:
            report += f"Pattern Type: {result['pattern_type']}\n"
            report += f"Patterns Found: {len(result['patterns'])}\n"
            report += f"Anomalies Found: {len(result['anomalies'])}\n"
            report += f"Security Flags: {', '.join(result['security_flags'])}\n"
            report += f"Confidence: {result['confidence']:.2f}\n\n"
        return report

def main():
    """Example usage"""
    recognizer = PatternRecognizer()
    
    # Example numerical data
    numerical_data = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0]
    
    # Example temporal data
    temporal_data = [
        ('2024-01-01', 100.0),
        ('2024-01-02', 150.0),
        ('2024-01-03', 125.0),
        ('2024-01-04', 200.0),
        ('2024-01-05', 175.0)
    ]
    
    results = []
    results.append(recognizer.analyze_numerical_patterns(numerical_data))
    results.append(recognizer.analyze_temporal_patterns(temporal_data))
    
    report = recognizer.generate_report(results)
    print("Pattern Recognition Report:")
    print(report)

if __name__ == "__main__":
    main()

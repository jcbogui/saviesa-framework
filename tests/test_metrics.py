#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Tests for Metrics Module
Saviesa Framework
"""

import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from utils.metrics import (
    calculate_r2,
    calculate_rmse,
    calculate_mae,
    calculate_aic,
    calculate_bic,
    diagnostic_divergence_rate
)

class TestMetrics(unittest.TestCase):
    """Test metric calculation functions"""
    
    def setUp(self):
        """Set up test data"""
        self.y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        self.y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
    
    def test_calculate_r2(self):
        """Test R² calculation"""
        r2 = calculate_r2(self.y_true, self.y_pred)
        
        self.assertGreater(r2, 0.9)
        self.assertLessEqual(r2, 1.0)
    
    def test_calculate_rmse(self):
        """Test RMSE calculation"""
        rmse = calculate_rmse(self.y_true, self.y_pred)
        
        self.assertGreater(rmse, 0)
        self.assertLess(rmse, 0.5)
    
    def test_calculate_mae(self):
        """Test MAE calculation"""
        mae = calculate_mae(self.y_true, self.y_pred)
        
        self.assertGreater(mae, 0)
        self.assertLess(mae, 0.5)
    
    def test_calculate_aic(self):
        """Test AIC calculation"""
        aic = calculate_aic(self.y_true, self.y_pred, n_params=3)
        
        self.assertIsInstance(aic, (int, float))
        self.assertLess(aic, 0)  # Should be negative for good fit
    
    def test_calculate_bic(self):
        """Test BIC calculation"""
        bic = calculate_bic(self.y_true, self.y_pred, n_params=3)
        
        self.assertIsInstance(bic, (int, float))

class TestDiagnosticDivergence(unittest.TestCase):
    """Test diagnostic divergence calculation"""
    
    def test_convergent_case(self):
        """Test fully convergent diagnostics"""
        factors1 = np.array(['L', 'M', 'L', 'M', 'L'])
        factors2 = np.array(['L', 'M', 'L', 'M', 'L'])
        
        result = diagnostic_divergence_rate(factors1, factors2)
        
        self.assertEqual(result['n_convergent'], 5)
        self.assertEqual(result['n_divergent'], 0)
        self.assertEqual(result['convergence_rate'], 100.0)
        self.assertEqual(result['divergence_rate'], 0.0)
    
    def test_divergent_case(self):
        """Test partially divergent diagnostics"""
        factors1 = np.array(['L', 'M', 'L', 'M', 'L'])
        factors2 = np.array(['M', 'M', 'L', 'L', 'M'])
        
        result = diagnostic_divergence_rate(factors1, factors2)
        
        self.assertEqual(result['n_total'], 5)
        self.assertEqual(result['n_convergent'], 2)
        self.assertEqual(result['n_divergent'], 3)
        self.assertEqual(result['convergence_rate'], 40.0)
        self.assertEqual(result['divergence_rate'], 60.0)
    
    def test_fully_divergent(self):
        """Test fully divergent diagnostics"""
        factors1 = np.array(['L', 'L', 'L'])
        factors2 = np.array(['M', 'M', 'M'])
        
        result = diagnostic_divergence_rate(factors1, factors2)
        
        self.assertEqual(result['n_convergent'], 0)
        self.assertEqual(result['n_divergent'], 3)
        self.assertEqual(result['divergence_rate'], 100.0)

class TestPerfectPrediction(unittest.TestCase):
    """Test metrics with perfect prediction"""
    
    def test_perfect_r2(self):
        """Test R² with perfect prediction"""
        y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        y_pred = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        
        r2 = calculate_r2(y_true, y_pred)
        self.assertEqual(r2, 1.0)
    
    def test_perfect_rmse(self):
        """Test RMSE with perfect prediction"""
        y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        y_pred = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        
        rmse = calculate_rmse(y_true, y_pred)
        self.assertAlmostEqual(rmse, 0.0, places=10)

if __name__ == '__main__':
    unittest.main()

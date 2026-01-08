#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Tests for Models Module
Saviesa Framework
"""

import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from utils.models import (
    AdditiveModel,
    InteractionModel,
    MultiplicativeModel,
    identify_limiting_factor
)

class TestAdditiveModel(unittest.TestCase):
    """Test AdditiveModel class"""
    
    def setUp(self):
        """Set up test data"""
        np.random.seed(42)
        self.n = 100
        self.X = np.random.rand(self.n, 2)
        self.y = 0.5 + 0.3 * self.X[:, 0] + 0.4 * self.X[:, 1] + np.random.normal(0, 0.01, self.n)
    
    def test_fit_predict(self):
        """Test model fitting and prediction"""
        model = AdditiveModel()
        model.fit(self.X, self.y)
        y_pred = model.predict(self.X)
        
        self.assertEqual(len(y_pred), self.n)
        self.assertTrue(model.is_fitted)
    
    def test_score(self):
        """Test R² score calculation"""
        model = AdditiveModel()
        model.fit(self.X, self.y)
        score = model.score(self.X, self.y)
        
        self.assertGreater(score, 0.9)  # Should have high R²
        self.assertLessEqual(score, 1.0)
    
    def test_coefficients(self):
        """Test coefficient extraction"""
        model = AdditiveModel()
        model.fit(self.X, self.y)
        coefs = model.get_coefficients()
        
        self.assertIn('intercept', coefs)
        self.assertIn('coefficients', coefs)
        self.assertEqual(len(coefs['coefficients']), 2)

class TestMultiplicativeModel(unittest.TestCase):
    """Test MultiplicativeModel class"""
    
    def setUp(self):
        """Set up test data"""
        np.random.seed(42)
        self.n = 100
        self.X = np.random.rand(self.n, 2) + 0.1  # Avoid zeros
        self.y = self.X[:, 0] * self.X[:, 1] * np.exp(np.random.normal(0, 0.01, self.n))
    
    def test_fit_predict(self):
        """Test model fitting and prediction"""
        model = MultiplicativeModel()
        model.fit(self.X, self.y)
        y_pred = model.predict(self.X)
        
        self.assertEqual(len(y_pred), self.n)
        self.assertTrue(model.is_fitted)
    
    def test_score(self):
        """Test R² score calculation"""
        model = MultiplicativeModel()
        model.fit(self.X, self.y)
        score = model.score(self.X, self.y)
        
        self.assertGreater(score, 0.95)  # Should have very high R² for multiplicative data
    
    def test_elasticities(self):
        """Test elasticity extraction"""
        model = MultiplicativeModel()
        model.fit(self.X, self.y)
        elast = model.get_elasticities()
        
        self.assertIn('intercept', elast)
        self.assertIn('elasticities', elast)
        self.assertEqual(len(elast['elasticities']), 2)
        
        # Elasticities should be close to 1.0 for true multiplicative data
        self.assertAlmostEqual(elast['elasticities'][0], 1.0, delta=0.1)
        self.assertAlmostEqual(elast['elasticities'][1], 1.0, delta=0.1)

class TestLimitingFactor(unittest.TestCase):
    """Test limiting factor identification"""
    
    def test_single_observation(self):
        """Test with single observation"""
        factors = np.array([0.8, 0.5, 0.9])
        limiting = identify_limiting_factor(factors, ['O', 'L', 'M'])
        
        self.assertEqual(limiting, 'L')
    
    def test_multiple_observations(self):
        """Test with multiple observations"""
        factors = np.array([
            [0.8, 0.5, 0.9],
            [0.3, 0.7, 0.6],
            [0.6, 0.8, 0.4]
        ])
        limiting = identify_limiting_factor(factors, ['O', 'L', 'M'])
        
        expected = np.array(['L', 'O', 'M'])
        np.testing.assert_array_equal(limiting, expected)
    
    def test_default_names(self):
        """Test with default factor names"""
        factors = np.array([0.8, 0.5, 0.9])
        limiting = identify_limiting_factor(factors)
        
        self.assertIn(limiting, ['F1', 'F2', 'F3'])

class TestInteractionModel(unittest.TestCase):
    """Test InteractionModel class"""
    
    def setUp(self):
        """Set up test data"""
        np.random.seed(42)
        self.n = 100
        self.X = np.random.rand(self.n, 2)
        self.y = 0.5 + 0.3 * self.X[:, 0] + 0.4 * self.X[:, 1] + \
                 0.2 * self.X[:, 0] * self.X[:, 1] + np.random.normal(0, 0.01, self.n)
    
    def test_fit_predict(self):
        """Test model fitting and prediction"""
        model = InteractionModel()
        model.fit(self.X, self.y)
        y_pred = model.predict(self.X)
        
        self.assertEqual(len(y_pred), self.n)
        self.assertTrue(model.is_fitted)
    
    def test_score(self):
        """Test R² score calculation"""
        model = InteractionModel()
        model.fit(self.X, self.y)
        score = model.score(self.X, self.y)
        
        self.assertGreater(score, 0.95)  # Should have high R² for interaction data

if __name__ == '__main__':
    unittest.main()

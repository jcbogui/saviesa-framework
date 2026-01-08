#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model Implementations
Saviesa Framework

This module provides implementations of additive, interaction, and multiplicative models.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class SaviesaModel:
    """Base class for Saviesa models"""
    
    def __init__(self):
        self.model = None
        self.is_fitted = False
    
    def fit(self, X, y):
        """Fit the model"""
        raise NotImplementedError
    
    def predict(self, X):
        """Make predictions"""
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        raise NotImplementedError
    
    def score(self, X, y):
        """Calculate R² score"""
        y_pred = self.predict(X)
        return r2_score(y, y_pred)

class AdditiveModel(SaviesaModel):
    """
    Additive model: F = α₀ + α₁·X₁ + α₂·X₂ + ... + αₙ·Xₙ
    
    Assumes full compensability between factors.
    """
    
    def fit(self, X, y):
        """
        Fit additive model
        
        Args:
            X: Feature matrix (n_samples, n_features)
            y: Target variable (n_samples,)
        """
        self.model = LinearRegression()
        self.model.fit(X, y)
        self.is_fitted = True
        return self
    
    def predict(self, X):
        """Predict using additive model"""
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        return self.model.predict(X)
    
    def get_coefficients(self):
        """Get model coefficients"""
        if not self.is_fitted:
            raise ValueError("Model must be fitted first")
        return {
            'intercept': self.model.intercept_,
            'coefficients': self.model.coef_
        }

class InteractionModel(SaviesaModel):
    """
    Interaction model: F = α₀ + α₁·X₁ + α₂·X₂ + α₁₂·(X₁×X₂)
    
    Allows partial non-compensability through interaction terms.
    """
    
    def fit(self, X, y):
        """
        Fit interaction model
        
        Args:
            X: Feature matrix (n_samples, n_features)
            y: Target variable (n_samples,)
        """
        # Add interaction terms (pairwise products)
        X_with_interactions = self._add_interactions(X)
        self.model = LinearRegression()
        self.model.fit(X_with_interactions, y)
        self.is_fitted = True
        self.n_features = X.shape[1]
        return self
    
    def _add_interactions(self, X):
        """Add pairwise interaction terms"""
        n_samples, n_features = X.shape
        interactions = []
        
        for i in range(n_features):
            for j in range(i + 1, n_features):
                interactions.append(X[:, i] * X[:, j])
        
        if interactions:
            return np.column_stack([X] + interactions)
        return X
    
    def predict(self, X):
        """Predict using interaction model"""
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        X_with_interactions = self._add_interactions(X)
        return self.model.predict(X_with_interactions)

class MultiplicativeModel(SaviesaModel):
    """
    Multiplicative model: log(F) = β₀ + β₁·log(X₁) + β₂·log(X₂) + ... + βₙ·log(Xₙ)
    
    Equivalent to: F = exp(β₀) × X₁^β₁ × X₂^β₂ × ... × Xₙ^βₙ
    
    Assumes full non-compensability (Liebig's Law of the Minimum).
    """
    
    def __init__(self, epsilon=1e-10):
        """
        Initialize multiplicative model
        
        Args:
            epsilon: Small constant to avoid log(0)
        """
        super().__init__()
        self.epsilon = epsilon
    
    def fit(self, X, y):
        """
        Fit multiplicative model using log-linear regression
        
        Args:
            X: Feature matrix (n_samples, n_features)
            y: Target variable (n_samples,)
        """
        # Log-transform inputs
        log_X = np.log(X + self.epsilon)
        log_y = np.log(y + self.epsilon)
        
        # Fit log-linear model
        self.model = LinearRegression()
        self.model.fit(log_X, log_y)
        self.is_fitted = True
        return self
    
    def predict(self, X):
        """Predict using multiplicative model"""
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction")
        
        # Log-transform inputs
        log_X = np.log(X + self.epsilon)
        
        # Predict in log space
        log_y_pred = self.model.predict(log_X)
        
        # Transform back to original scale
        y_pred = np.exp(log_y_pred)
        
        return y_pred
    
    def get_elasticities(self):
        """
        Get elasticities (β coefficients)
        
        Returns:
            dict: Intercept and elasticities
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted first")
        return {
            'intercept': self.model.intercept_,
            'elasticities': self.model.coef_
        }

def identify_limiting_factor(factors, factor_names=None):
    """
    Identify limiting factor using Liebig's Law of the Minimum
    
    Args:
        factors: Array of factor values (n_samples, n_factors) or (n_factors,)
        factor_names: List of factor names (default: ['F1', 'F2', ...])
    
    Returns:
        str or array: Name(s) of limiting factor(s)
    
    Example:
        >>> factors = np.array([[0.8, 0.5, 0.9], [0.3, 0.7, 0.6]])
        >>> identify_limiting_factor(factors, ['O', 'L', 'M'])
        array(['L', 'O'], dtype='<U1')
    """
    factors = np.asarray(factors)
    
    if factor_names is None:
        n_factors = factors.shape[-1] if factors.ndim > 1 else len(factors)
        factor_names = [f'F{i+1}' for i in range(n_factors)]
    
    factor_names = np.array(factor_names)
    
    if factors.ndim == 1:
        # Single observation
        min_idx = np.argmin(factors)
        return factor_names[min_idx]
    else:
        # Multiple observations
        min_indices = np.argmin(factors, axis=1)
        return factor_names[min_indices]

def compare_models(X, y, model_names=None):
    """
    Compare additive, interaction, and multiplicative models
    
    Args:
        X: Feature matrix (n_samples, n_features)
        y: Target variable (n_samples,)
        model_names: Optional custom model names
    
    Returns:
        pd.DataFrame: Comparison results
    """
    import pandas as pd
    
    if model_names is None:
        model_names = ['Additive', 'Interaction', 'Multiplicative']
    
    # Fit models
    models = [
        AdditiveModel(),
        InteractionModel(),
        MultiplicativeModel()
    ]
    
    results = []
    for model, name in zip(models, model_names):
        model.fit(X, y)
        y_pred = model.predict(X)
        
        r2 = r2_score(y, y_pred)
        rmse = np.sqrt(mean_squared_error(y, y_pred))
        mae = mean_absolute_error(y, y_pred)
        
        results.append({
            'Model': name,
            'R²': r2,
            'RMSE': rmse,
            'MAE': mae
        })
    
    return pd.DataFrame(results)

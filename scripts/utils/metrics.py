#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Performance Metrics
Saviesa Framework

This module provides performance metrics for model evaluation.
"""

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import LeaveOneOut

def calculate_r2(y_true, y_pred):
    """
    Calculate R² (coefficient of determination)
    
    Args:
        y_true: True values
        y_pred: Predicted values
    
    Returns:
        float: R² score
    """
    return r2_score(y_true, y_pred)

def calculate_rmse(y_true, y_pred):
    """
    Calculate RMSE (Root Mean Squared Error)
    
    Args:
        y_true: True values
        y_pred: Predicted values
    
    Returns:
        float: RMSE
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))

def calculate_mae(y_true, y_pred):
    """
    Calculate MAE (Mean Absolute Error)
    
    Args:
        y_true: True values
        y_pred: Predicted values
    
    Returns:
        float: MAE
    """
    return mean_absolute_error(y_true, y_pred)

def calculate_aic(y_true, y_pred, n_params):
    """
    Calculate AIC (Akaike Information Criterion)
    
    Args:
        y_true: True values
        y_pred: Predicted values
        n_params: Number of model parameters (including intercept)
    
    Returns:
        float: AIC
    """
    n = len(y_true)
    rss = np.sum((y_true - y_pred)**2)
    aic = n * np.log(rss / n) + 2 * n_params
    return aic

def calculate_bic(y_true, y_pred, n_params):
    """
    Calculate BIC (Bayesian Information Criterion)
    
    Args:
        y_true: True values
        y_pred: Predicted values
        n_params: Number of model parameters (including intercept)
    
    Returns:
        float: BIC
    """
    n = len(y_true)
    rss = np.sum((y_true - y_pred)**2)
    bic = n * np.log(rss / n) + n_params * np.log(n)
    return bic

def loocv_validation(model, X, y):
    """
    Perform Leave-One-Out Cross-Validation
    
    Args:
        model: Model instance with fit() and predict() methods
        X: Feature matrix
        y: Target variable
    
    Returns:
        dict: LOOCV results (r2, rmse, mae, predictions)
    """
    loo = LeaveOneOut()
    predictions = []
    actuals = []
    
    for train_idx, test_idx in loo.split(X):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        # Fit model on training data
        model.fit(X_train, y_train)
        
        # Predict on test data
        y_pred = model.predict(X_test)
        
        predictions.append(y_pred[0] if hasattr(y_pred, '__len__') else y_pred)
        actuals.append(y_test[0] if hasattr(y_test, '__len__') else y_test)
    
    predictions = np.array(predictions)
    actuals = np.array(actuals)
    
    r2_loocv = calculate_r2(actuals, predictions)
    rmse_loocv = calculate_rmse(actuals, predictions)
    mae_loocv = calculate_mae(actuals, predictions)
    
    return {
        'r2_loocv': r2_loocv,
        'rmse_loocv': rmse_loocv,
        'mae_loocv': mae_loocv,
        'predictions': predictions,
        'actuals': actuals
    }

def calculate_all_metrics(y_true, y_pred, n_params=None):
    """
    Calculate all standard metrics
    
    Args:
        y_true: True values
        y_pred: Predicted values
        n_params: Number of parameters (for AIC/BIC)
    
    Returns:
        dict: All metrics
    """
    metrics = {
        'r2': calculate_r2(y_true, y_pred),
        'rmse': calculate_rmse(y_true, y_pred),
        'mae': calculate_mae(y_true, y_pred)
    }
    
    if n_params is not None:
        metrics['aic'] = calculate_aic(y_true, y_pred, n_params)
        metrics['bic'] = calculate_bic(y_true, y_pred, n_params)
    
    return metrics

def compare_predictions(y_true, y_pred1, y_pred2, model1_name='Model 1', model2_name='Model 2'):
    """
    Compare predictions from two models
    
    Args:
        y_true: True values
        y_pred1: Predictions from model 1
        y_pred2: Predictions from model 2
        model1_name: Name of model 1
        model2_name: Name of model 2
    
    Returns:
        dict: Comparison results
    """
    metrics1 = calculate_all_metrics(y_true, y_pred1)
    metrics2 = calculate_all_metrics(y_true, y_pred2)
    
    comparison = {
        model1_name: metrics1,
        model2_name: metrics2,
        'gains': {
            'delta_r2': metrics2['r2'] - metrics1['r2'],
            'delta_rmse': metrics2['rmse'] - metrics1['rmse'],
            'delta_mae': metrics2['mae'] - metrics1['mae'],
            'pct_rmse_improvement': ((metrics1['rmse'] - metrics2['rmse']) / metrics1['rmse']) * 100,
            'pct_mae_improvement': ((metrics1['mae'] - metrics2['mae']) / metrics1['mae']) * 100
        }
    }
    
    return comparison

def diagnostic_divergence_rate(limiting_factors1, limiting_factors2):
    """
    Calculate diagnostic divergence rate between two methods
    
    Args:
        limiting_factors1: Limiting factors from method 1 (array)
        limiting_factors2: Limiting factors from method 2 (array)
    
    Returns:
        dict: Divergence statistics
    """
    limiting_factors1 = np.asarray(limiting_factors1)
    limiting_factors2 = np.asarray(limiting_factors2)
    
    convergent = (limiting_factors1 == limiting_factors2)
    divergent = ~convergent
    
    n_total = len(limiting_factors1)
    n_convergent = np.sum(convergent)
    n_divergent = np.sum(divergent)
    
    return {
        'n_total': n_total,
        'n_convergent': n_convergent,
        'n_divergent': n_divergent,
        'convergence_rate': (n_convergent / n_total) * 100,
        'divergence_rate': (n_divergent / n_total) * 100,
        'convergent_mask': convergent,
        'divergent_mask': divergent
    }

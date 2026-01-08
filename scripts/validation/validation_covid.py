#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COVID-19 Validation Script
Saviesa Framework - Article 2 Empirical Validation

This script validates the Saviesa multiplicative model on COVID-19 vaccination data
(n=65 French departments) and compares it to additive and interaction models.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_covid_data(filepath='../../data/processed/Article2_Dataset_COVID.csv'):
    """Load COVID-19 dataset"""
    df = pd.read_csv(filepath)
    print(f"✅ Dataset loaded: n={len(df)} departments")
    return df

def fit_additive_model(X_L, X_M, y):
    """
    Fit additive model: F = α₀ + α_L·L + α_M·M
    
    Args:
        X_L: Levier variable (n×1)
        X_M: Milieu variable (n×1)
        y: Performance variable (n,)
    
    Returns:
        dict: Model results (model, predictions, metrics, coefficients)
    """
    X = np.column_stack([X_L, X_M])
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    
    # Calculate AIC
    n = len(y)
    k = 3  # 2 variables + intercept
    rss = np.sum((y - y_pred)**2)
    aic = n * np.log(rss / n) + 2 * k
    
    return {
        'model': model,
        'y_pred': y_pred,
        'r2': r2,
        'rmse': rmse,
        'mae': mae,
        'aic': aic,
        'coefficients': {
            'intercept': model.intercept_,
            'alpha_L': model.coef_[0],
            'alpha_M': model.coef_[1]
        }
    }

def fit_interaction_model(X_L, X_M, y):
    """
    Fit interaction model: F = α₀ + α_L·L + α_M·M + α_I·(L×M)
    
    Args:
        X_L: Levier variable (n×1)
        X_M: Milieu variable (n×1)
        y: Performance variable (n,)
    
    Returns:
        dict: Model results
    """
    X = np.column_stack([X_L, X_M, X_L * X_M])
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    
    n = len(y)
    k = 4  # 3 variables + intercept
    rss = np.sum((y - y_pred)**2)
    aic = n * np.log(rss / n) + 2 * k
    
    return {
        'model': model,
        'y_pred': y_pred,
        'r2': r2,
        'rmse': rmse,
        'mae': mae,
        'aic': aic,
        'coefficients': {
            'intercept': model.intercept_,
            'alpha_L': model.coef_[0],
            'alpha_M': model.coef_[1],
            'alpha_I': model.coef_[2]
        }
    }

def fit_multiplicative_model(X_L, X_M, y):
    """
    Fit multiplicative model: log(F) = β₀ + β_L·log(L) + β_M·log(M)
    
    Args:
        X_L: Levier variable (n×1)
        X_M: Milieu variable (n×1)
        y: Performance variable (n,)
    
    Returns:
        dict: Model results
    """
    # Log-transformation (avoid log(0))
    log_L = np.log(X_L + 1e-10)
    log_M = np.log(X_M + 1e-10)
    log_F = np.log(y + 1e-10)
    
    X = np.column_stack([log_L, log_M])
    model = LinearRegression()
    model.fit(X, log_F)
    
    # Predictions in original scale
    log_F_pred = model.predict(X)
    y_pred = np.exp(log_F_pred)
    
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    mae = mean_absolute_error(y, y_pred)
    
    n = len(y)
    k = 3  # 2 variables + intercept
    rss = np.sum((y - y_pred)**2)
    aic = n * np.log(rss / n) + 2 * k
    
    return {
        'model': model,
        'y_pred': y_pred,
        'r2': r2,
        'rmse': rmse,
        'mae': mae,
        'aic': aic,
        'coefficients': {
            'intercept': model.intercept_,
            'beta_L': model.coef_[0],
            'beta_M': model.coef_[1]
        }
    }

def main():
    """Main validation script"""
    print("\n" + "="*70)
    print("SAVIESA FRAMEWORK - COVID-19 VALIDATION")
    print("="*70)
    
    # Load data
    df = load_covid_data()
    
    X_L = df['L'].values
    X_M = df['M'].values
    y = df['F'].values
    
    print("\n" + "="*70)
    print("MODEL COMPARISON")
    print("="*70)
    
    # Model M0: Additive
    print("\n[1/3] Model M0 (Additive)...")
    m0 = fit_additive_model(X_L, X_M, y)
    print(f"  R² = {m0['r2']:.4f}")
    print(f"  RMSE = {m0['rmse']:.4f}")
    print(f"  MAE = {m0['mae']:.4f}")
    print(f"  AIC = {m0['aic']:.0f}")
    
    # Model M1: Interaction
    print("\n[2/3] Model M1 (Interaction)...")
    m1 = fit_interaction_model(X_L, X_M, y)
    print(f"  R² = {m1['r2']:.4f}")
    print(f"  RMSE = {m1['rmse']:.4f}")
    print(f"  MAE = {m1['mae']:.4f}")
    print(f"  AIC = {m1['aic']:.0f}")
    
    # Model M2: Multiplicative
    print("\n[3/3] Model M2 (Multiplicative - Saviesa)...")
    m2 = fit_multiplicative_model(X_L, X_M, y)
    print(f"  R² = {m2['r2']:.4f}")
    print(f"  RMSE = {m2['rmse']:.4f}")
    print(f"  MAE = {m2['mae']:.4f}")
    print(f"  AIC = {m2['aic']:.0f}")
    
    # Summary
    print("\n" + "="*70)
    print("RESULTS SUMMARY")
    print("="*70)
    print(f"\n{'Model':<25} {'R²':<10} {'RMSE':<10} {'MAE':<10} {'AIC':<10}")
    print("-"*70)
    print(f"{'M0 (Additive)':<25} {m0['r2']:<10.4f} {m0['rmse']:<10.4f} {m0['mae']:<10.4f} {m0['aic']:<10.0f}")
    print(f"{'M1 (Interaction)':<25} {m1['r2']:<10.4f} {m1['rmse']:<10.4f} {m1['mae']:<10.4f} {m1['aic']:<10.0f}")
    print(f"{'M2 (Multiplicative)':<25} {m2['r2']:<10.4f} {m2['rmse']:<10.4f} {m2['mae']:<10.4f} {m2['aic']:<10.0f}")
    
    # Gains
    print("\n" + "="*70)
    print("MULTIPLICATIVE MODEL GAINS")
    print("="*70)
    print(f"Δ R² (vs Additive):     +{(m2['r2'] - m0['r2'])*100:.2f}%")
    print(f"Δ RMSE (vs Additive):   {((m2['rmse'] - m0['rmse'])/m0['rmse'])*100:.1f}%")
    print(f"Δ AIC (vs Additive):    {m2['aic'] - m0['aic']:.0f}")
    
    # Save results
    results = pd.DataFrame({
        'Model': ['M0 (Additive)', 'M1 (Interaction)', 'M2 (Multiplicative)'],
        'R²': [m0['r2'], m1['r2'], m2['r2']],
        'RMSE': [m0['rmse'], m1['rmse'], m2['rmse']],
        'MAE': [m0['mae'], m1['mae'], m2['mae']],
        'AIC': [m0['aic'], m1['aic'], m2['aic']]
    })
    
    output_dir = '../../results'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'Validation_COVID_Results.csv')
    results.to_csv(output_file, index=False)
    
    print(f"\n✅ Results saved: {output_file}")
    print("\n" + "="*70)
    print("VALIDATION COMPLETE")
    print("="*70)

if __name__ == "__main__":
    main()

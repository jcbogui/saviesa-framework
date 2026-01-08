#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagnostic Différentiel Script
Saviesa Framework - Article 2 Section 6

This script compares multiplicative vs additive diagnostics and calculates
the divergence rate (percentage of different recommendations).
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_covid_data(filepath='../../data/processed/Article2_Dataset_COVID.csv'):
    """Load COVID-19 dataset"""
    df = pd.read_csv(filepath)
    return df

def identify_limiting_factor_multiplicative(O, L, M):
    """
    Identify limiting factor using multiplicative logic: min(O, L, M)
    
    Args:
        O, L, M: Factor values (scalars or arrays)
    
    Returns:
        str or array: Limiting factor name(s)
    """
    factors = {'O': O, 'L': L, 'M': M}
    
    if isinstance(O, (int, float)):
        return min(factors, key=factors.get)
    else:
        # Vectorized for arrays
        factors_array = np.column_stack([O, L, M])
        min_indices = np.argmin(factors_array, axis=1)
        factor_names = np.array(['O', 'L', 'M'])
        return factor_names[min_indices]

def identify_limiting_factor_additive(alpha_O, alpha_L, alpha_M, O, L, M):
    """
    Identify limiting factor using additive logic: max(α_i × X_i)
    
    Args:
        alpha_O, alpha_L, alpha_M: Coefficients from additive regression
        O, L, M: Factor values (scalars or arrays)
    
    Returns:
        str or array: Limiting factor name(s)
    """
    contributions = {
        'O': alpha_O * O,
        'L': alpha_L * L,
        'M': alpha_M * M
    }
    
    if isinstance(O, (int, float)):
        return max(contributions, key=contributions.get)
    else:
        # Vectorized for arrays
        contrib_array = np.column_stack([contributions['O'], contributions['L'], contributions['M']])
        max_indices = np.argmax(contrib_array, axis=1)
        factor_names = np.array(['O', 'L', 'M'])
        return factor_names[max_indices]

def calculate_efficiency_gain(O, L, M, limiting_mult, limiting_add):
    """
    Calculate efficiency gain ratio for divergent cases
    
    Efficiency gain = (Investment in correct factor) / (Investment in wrong factor)
    
    Args:
        O, L, M: Factor values
        limiting_mult: Limiting factor (multiplicative)
        limiting_add: Limiting factor (additive)
    
    Returns:
        float: Efficiency gain ratio
    """
    factors = {'O': O, 'L': L, 'M': M}
    
    if limiting_mult == limiting_add:
        return 1.0  # No divergence, no gain
    
    # Multiplicative logic: invest in min factor
    correct_factor_value = factors[limiting_mult]
    
    # Additive logic: invest in max contribution factor
    wrong_factor_value = factors[limiting_add]
    
    # Efficiency gain = how much more effective is correct investment
    # Simplified: ratio of marginal returns
    # In multiplicative model, investing in limiting factor has highest return
    gain = wrong_factor_value / correct_factor_value if correct_factor_value > 0 else 1.0
    
    return gain

def main():
    """Main diagnostic comparison script"""
    print("\n" + "="*70)
    print("SAVIESA FRAMEWORK - DIAGNOSTIC DIFFÉRENTIEL")
    print("="*70)
    
    # Load data
    df = load_covid_data()
    print(f"✅ Dataset loaded: n={len(df)} departments")
    
    # For COVID: O=1 (fixed), so we focus on L and M
    L = df['L'].values
    M = df['M'].values
    F = df['F'].values
    O = np.ones_like(L)  # O=1 for COVID
    
    # Fit additive model to get coefficients
    X_add = np.column_stack([L, M])
    model_add = LinearRegression()
    model_add.fit(X_add, F)
    
    alpha_L = model_add.coef_[0]
    alpha_M = model_add.coef_[1]
    
    print("\n" + "="*70)
    print("ADDITIVE MODEL COEFFICIENTS")
    print("="*70)
    print(f"α_L = {alpha_L:.4f}")
    print(f"α_M = {alpha_M:.4f}")
    
    # Identify limiting factors
    print("\n" + "="*70)
    print("LIMITING FACTOR IDENTIFICATION")
    print("="*70)
    
    # Multiplicative diagnostic
    limiting_mult = identify_limiting_factor_multiplicative(O, L, M)
    
    # Additive diagnostic (for COVID, simplified to L vs M)
    contrib_L = alpha_L * L
    contrib_M = alpha_M * M
    limiting_add = np.where(contrib_L > contrib_M, 'L', 'M')
    
    # Calculate convergence/divergence
    convergent = (limiting_mult == limiting_add)
    divergent = ~convergent
    
    convergence_rate = np.mean(convergent) * 100
    divergence_rate = np.mean(divergent) * 100
    
    print(f"\n✅ Convergent cases: {np.sum(convergent)}/{len(df)} ({convergence_rate:.1f}%)")
    print(f"⚠️  Divergent cases:  {np.sum(divergent)}/{len(df)} ({divergence_rate:.1f}%)")
    
    # Analyze divergent cases
    if np.sum(divergent) > 0:
        print("\n" + "="*70)
        print("DIVERGENT CASES ANALYSIS")
        print("="*70)
        
        divergent_df = df[divergent].copy()
        divergent_df['limiting_mult'] = limiting_mult[divergent]
        divergent_df['limiting_add'] = limiting_add[divergent]
        
        print(f"\nSample divergent departments (first 5):")
        print(divergent_df[['department_name', 'L', 'M', 'limiting_mult', 'limiting_add']].head())
        
        # Calculate efficiency gains
        efficiency_gains = []
        for i in np.where(divergent)[0]:
            gain = calculate_efficiency_gain(
                O[i], L[i], M[i],
                limiting_mult[i], limiting_add[i]
            )
            efficiency_gains.append(gain)
        
        avg_efficiency_gain = np.mean(efficiency_gains)
        median_efficiency_gain = np.median(efficiency_gains)
        
        print(f"\n📊 Efficiency Gain Statistics:")
        print(f"   Mean:   {avg_efficiency_gain:.1f}×")
        print(f"   Median: {median_efficiency_gain:.1f}×")
        print(f"   Range:  {np.min(efficiency_gains):.1f}× - {np.max(efficiency_gains):.1f}×")
    
    # Distribution of limiting factors
    print("\n" + "="*70)
    print("LIMITING FACTOR DISTRIBUTION")
    print("="*70)
    
    print("\nMultiplicative diagnostic:")
    unique_mult, counts_mult = np.unique(limiting_mult, return_counts=True)
    for factor, count in zip(unique_mult, counts_mult):
        print(f"  {factor}: {count} departments ({count/len(df)*100:.1f}%)")
    
    print("\nAdditive diagnostic:")
    unique_add, counts_add = np.unique(limiting_add, return_counts=True)
    for factor, count in zip(unique_add, counts_add):
        print(f"  {factor}: {count} departments ({count/len(df)*100:.1f}%)")
    
    # Save results
    results = pd.DataFrame({
        'department_code': df['department_code'],
        'department_name': df['department_name'],
        'L': L,
        'M': M,
        'F': F,
        'limiting_multiplicative': limiting_mult,
        'limiting_additive': limiting_add,
        'convergent': convergent,
        'divergent': divergent
    })
    
    output_dir = '../../results'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'Diagnostic_Differentiel_Results.csv')
    results.to_csv(output_file, index=False)
    
    # Summary statistics
    summary = pd.DataFrame({
        'Metric': [
            'Total departments',
            'Convergent cases',
            'Divergent cases',
            'Convergence rate (%)',
            'Divergence rate (%)',
            'Avg efficiency gain (×)'
        ],
        'Value': [
            len(df),
            np.sum(convergent),
            np.sum(divergent),
            convergence_rate,
            divergence_rate,
            avg_efficiency_gain if np.sum(divergent) > 0 else 0
        ]
    })
    
    summary_file = os.path.join(output_dir, 'Diagnostic_Summary.csv')
    summary.to_csv(summary_file, index=False)
    
    print(f"\n✅ Results saved:")
    print(f"   - {output_file}")
    print(f"   - {summary_file}")
    
    print("\n" + "="*70)
    print("KEY FINDING")
    print("="*70)
    print(f"\n🎯 {divergence_rate:.1f}% of departments receive DIFFERENT recommendations")
    print(f"   under multiplicative vs additive diagnostics.")
    print(f"\n💡 Average efficiency gain from correct diagnosis: {avg_efficiency_gain:.1f}×")
    print(f"   (Investing in the right factor is {avg_efficiency_gain:.1f}× more effective)")
    
    print("\n" + "="*70)
    print("DIAGNOSTIC COMPARISON COMPLETE")
    print("="*70)

if __name__ == "__main__":
    main()

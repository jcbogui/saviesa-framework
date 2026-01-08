#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualization Functions
Saviesa Framework

This module provides plotting functions for Saviesa framework visualizations.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

def plot_scatter(y_true, y_pred, title='Observed vs Predicted', 
                 xlabel='Observed', ylabel='Predicted', 
                 save_path=None, show=True):
    """
    Plot scatter plot of observed vs predicted values
    
    Args:
        y_true: True values
        y_pred: Predicted values
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        save_path: Path to save figure (optional)
        show: Whether to display plot
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Scatter plot
    ax.scatter(y_true, y_pred, alpha=0.6, edgecolors='k', linewidth=0.5)
    
    # Perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect prediction')
    
    # Labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # R² annotation
    from sklearn.metrics import r2_score
    r2 = r2_score(y_true, y_pred)
    ax.text(0.05, 0.95, f'R² = {r2:.4f}', 
            transform=ax.transAxes, fontsize=12,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Figure saved: {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()

def plot_distribution(data, labels, title='Distribution', 
                      xlabel='Category', ylabel='Count',
                      save_path=None, show=True):
    """
    Plot bar chart of distribution
    
    Args:
        data: Data values (counts)
        labels: Category labels
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        save_path: Path to save figure
        show: Whether to display plot
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = sns.color_palette("Set2", len(labels))
    bars = ax.bar(labels, data, color=colors, edgecolor='black', linewidth=1.2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Figure saved: {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()

def plot_model_comparison(models_results, metric='r2',
                          title='Model Comparison',
                          save_path=None, show=True):
    """
    Plot model comparison bar chart
    
    Args:
        models_results: Dict of {model_name: {metric: value}}
        metric: Metric to plot ('r2', 'rmse', 'mae')
        title: Plot title
        save_path: Path to save figure
        show: Whether to display plot
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    model_names = list(models_results.keys())
    values = [models_results[name][metric] for name in model_names]
    
    colors = sns.color_palette("viridis", len(model_names))
    bars = ax.bar(model_names, values, color=colors, edgecolor='black', linewidth=1.2)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.4f}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    metric_labels = {
        'r2': 'R²',
        'rmse': 'RMSE',
        'mae': 'MAE',
        'aic': 'AIC'
    }
    
    ax.set_ylabel(metric_labels.get(metric, metric), fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Figure saved: {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()

def plot_residuals(y_true, y_pred, title='Residual Plot',
                   save_path=None, show=True):
    """
    Plot residuals (y_true - y_pred) vs predicted values
    
    Args:
        y_true: True values
        y_pred: Predicted values
        title: Plot title
        save_path: Path to save figure
        show: Whether to display plot
    """
    residuals = y_true - y_pred
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5)
    ax.axhline(y=0, color='r', linestyle='--', lw=2)
    
    ax.set_xlabel('Predicted values', fontsize=12)
    ax.set_ylabel('Residuals', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Figure saved: {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()

def plot_heatmap(data, row_labels, col_labels, title='Heatmap',
                 cmap='YlOrRd', save_path=None, show=True):
    """
    Plot heatmap
    
    Args:
        data: 2D array
        row_labels: Row labels
        col_labels: Column labels
        title: Plot title
        cmap: Colormap
        save_path: Path to save figure
        show: Whether to display plot
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    im = ax.imshow(data, cmap=cmap, aspect='auto')
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(col_labels)))
    ax.set_yticks(np.arange(len(row_labels)))
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)
    
    # Rotate x labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    
    # Add title
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"✅ Figure saved: {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()

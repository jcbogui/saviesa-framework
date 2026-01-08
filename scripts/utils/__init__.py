"""
Saviesa Framework - Utility Modules

This package provides utility functions for the Saviesa framework.
"""

from .models import (
    AdditiveModel,
    InteractionModel,
    MultiplicativeModel,
    identify_limiting_factor,
    compare_models
)

from .metrics import (
    calculate_r2,
    calculate_rmse,
    calculate_mae,
    calculate_aic,
    calculate_bic,
    loocv_validation,
    calculate_all_metrics,
    compare_predictions,
    diagnostic_divergence_rate
)

from .visualization import (
    plot_scatter,
    plot_distribution,
    plot_model_comparison,
    plot_residuals,
    plot_heatmap
)

__all__ = [
    # Models
    'AdditiveModel',
    'InteractionModel',
    'MultiplicativeModel',
    'identify_limiting_factor',
    'compare_models',
    # Metrics
    'calculate_r2',
    'calculate_rmse',
    'calculate_mae',
    'calculate_aic',
    'calculate_bic',
    'loocv_validation',
    'calculate_all_metrics',
    'compare_predictions',
    'diagnostic_divergence_rate',
    # Visualization
    'plot_scatter',
    'plot_distribution',
    'plot_model_comparison',
    'plot_residuals',
    'plot_heatmap'
]

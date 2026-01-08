# API Reference

Complete reference for the Saviesa Framework modules, classes, and functions.

---

## 📋 Table of Contents

1. [Models Module](#models-module)
2. [Metrics Module](#metrics-module)
3. [Visualization Module](#visualization-module)
4. [Utils Module](#utils-module)

---

## 🔧 Models Module

**Location**: `scripts/utils/models.py`

### SaviesaModel

Base class for Saviesa multiplicative models.

```python
class SaviesaModel:
    """Base class for Saviesa multiplicative performance models"""
    
    def __init__(self):
        """Initialize model"""
        pass
    
    def fit(self, X, y):
        """
        Fit the model to data
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data (L, M) or (O, L, M)
        y : array-like, shape (n_samples,)
            Target values (F)
            
        Returns
        -------
        self : object
            Fitted model
        """
        pass
    
    def predict(self, X):
        """
        Predict using the fitted model
        
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Samples to predict
            
        Returns
        -------
        y_pred : array, shape (n_samples,)
            Predicted values
        """
        pass
```

---

### MultiplicativeModel

Multiplicative model: F = L × M

```python
class MultiplicativeModel(SaviesaModel):
    """
    Multiplicative model with two factors
    
    Model: log(F) = β₀ + β_L·log(L) + β_M·log(M)
    
    Attributes
    ----------
    coef_ : array, shape (2,)
        Coefficients [β_L, β_M]
    intercept_ : float
        Intercept β₀
    r2_score_ : float
        R² score on training data
        
    Examples
    --------
    >>> from scripts.utils.models import MultiplicativeModel
    >>> import numpy as np
    >>> 
    >>> # Generate synthetic data
    >>> n = 100
    >>> L = np.random.uniform(0.5, 1.0, n)
    >>> M = np.random.uniform(0.4, 0.9, n)
    >>> F = L * M
    >>> 
    >>> # Fit model
    >>> model = MultiplicativeModel()
    >>> model.fit(np.column_stack([L, M]), F)
    >>> 
    >>> # Predict
    >>> F_pred = model.predict(np.column_stack([L, M]))
    >>> print(f"R² = {model.r2_score_:.4f}")
    """
    
    def __init__(self, epsilon=1e-6):
        """
        Initialize multiplicative model
        
        Parameters
        ----------
        epsilon : float, default=1e-6
            Small constant to add before log transformation
            to avoid log(0)
        """
        super().__init__()
        self.epsilon = epsilon
        self.model_ = None
        
    def fit(self, X, y):
        """
        Fit multiplicative model
        
        Parameters
        ----------
        X : array-like, shape (n_samples, 2)
            Features [L, M]
        y : array-like, shape (n_samples,)
            Target F
            
        Returns
        -------
        self : object
        """
        from sklearn.linear_model import LinearRegression
        
        # Log transformation
        X_log = np.log(X + self.epsilon)
        y_log = np.log(y + self.epsilon)
        
        # Fit linear model in log space
        self.model_ = LinearRegression()
        self.model_.fit(X_log, y_log)
        
        # Store coefficients
        self.coef_ = self.model_.coef_
        self.intercept_ = self.model_.intercept_
        self.r2_score_ = self.model_.score(X_log, y_log)
        
        return self
    
    def predict(self, X):
        """
        Predict F values
        
        Parameters
        ----------
        X : array-like, shape (n_samples, 2)
            Features [L, M]
            
        Returns
        -------
        y_pred : array, shape (n_samples,)
            Predicted F values
        """
        X_log = np.log(X + self.epsilon)
        y_log_pred = self.model_.predict(X_log)
        return np.exp(y_log_pred)
```

---

### AdditiveModel

Additive model: F = β₀ + β_L·L + β_M·M

```python
class AdditiveModel(SaviesaModel):
    """
    Additive linear model for comparison
    
    Model: F = β₀ + β_L·L + β_M·M
    
    Attributes
    ----------
    coef_ : array, shape (2,)
        Coefficients [β_L, β_M]
    intercept_ : float
        Intercept β₀
    r2_score_ : float
        R² score on training data
        
    Examples
    --------
    >>> from scripts.utils.models import AdditiveModel
    >>> import numpy as np
    >>> 
    >>> # Generate synthetic data
    >>> n = 100
    >>> L = np.random.uniform(0.5, 1.0, n)
    >>> M = np.random.uniform(0.4, 0.9, n)
    >>> F = 0.3 + 0.4*L + 0.5*M
    >>> 
    >>> # Fit model
    >>> model = AdditiveModel()
    >>> model.fit(np.column_stack([L, M]), F)
    >>> 
    >>> # Predict
    >>> F_pred = model.predict(np.column_stack([L, M]))
    >>> print(f"R² = {model.r2_score_:.4f}")
    """
    
    def __init__(self):
        """Initialize additive model"""
        super().__init__()
        self.model_ = None
        
    def fit(self, X, y):
        """
        Fit additive model
        
        Parameters
        ----------
        X : array-like, shape (n_samples, 2)
            Features [L, M]
        y : array-like, shape (n_samples,)
            Target F
            
        Returns
        -------
        self : object
        """
        from sklearn.linear_model import LinearRegression
        
        self.model_ = LinearRegression()
        self.model_.fit(X, y)
        
        self.coef_ = self.model_.coef_
        self.intercept_ = self.model_.intercept_
        self.r2_score_ = self.model_.score(X, y)
        
        return self
    
    def predict(self, X):
        """
        Predict F values
        
        Parameters
        ----------
        X : array-like, shape (n_samples, 2)
            Features [L, M]
            
        Returns
        -------
        y_pred : array, shape (n_samples,)
            Predicted F values
        """
        return self.model_.predict(X)
```

---

## 📊 Metrics Module

**Location**: `scripts/utils/metrics.py`

### compute_r2

```python
def compute_r2(y_true, y_pred):
    """
    Compute R² (coefficient of determination)
    
    Parameters
    ----------
    y_true : array-like, shape (n_samples,)
        True values
    y_pred : array-like, shape (n_samples,)
        Predicted values
        
    Returns
    -------
    r2 : float
        R² score
        
    Examples
    --------
    >>> y_true = np.array([1.0, 2.0, 3.0, 4.0])
    >>> y_pred = np.array([1.1, 1.9, 3.2, 3.8])
    >>> r2 = compute_r2(y_true, y_pred)
    >>> print(f"R² = {r2:.4f}")
    """
    from sklearn.metrics import r2_score
    return r2_score(y_true, y_pred)
```

### identify_limiting_factors

```python
def identify_limiting_factors(df, factors=['L', 'M']):
    """
    Identify which factor limits performance
    
    Parameters
    ----------
    df : pandas.DataFrame
        Dataset with factor columns
    factors : list of str, default=['L', 'M']
        Factor column names
        
    Returns
    -------
    limiting : pandas.Series
        Limiting factor for each observation
        
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'L': [0.8, 0.6, 0.9],
    ...     'M': [0.7, 0.8, 0.5]
    ... })
    >>> limiting = identify_limiting_factors(df)
    >>> print(limiting)
    0    M
    1    L
    2    M
    dtype: object
    """
    return df[factors].idxmin(axis=1)
```

### compute_improvement

```python
def compute_improvement(r2_mult, r2_add):
    """
    Compute percentage improvement of multiplicative over additive
    
    Parameters
    ----------
    r2_mult : float
        R² of multiplicative model
    r2_add : float
        R² of additive model
        
    Returns
    -------
    improvement : float
        Percentage improvement
        
    Examples
    --------
    >>> r2_mult = 0.95
    >>> r2_add = 0.90
    >>> improvement = compute_improvement(r2_mult, r2_add)
    >>> print(f"Improvement: {improvement:.2f}%")
    Improvement: 5.56%
    """
    return ((r2_mult - r2_add) / r2_add) * 100
```

---

## 📈 Visualization Module

**Location**: `scripts/utils/visualization.py`

### plot_scatter_LM

```python
def plot_scatter_LM(df, title='Saviesa Framework', 
                    save_path=None, figsize=(10, 6)):
    """
    Create scatter plot of L vs M colored by F
    
    Parameters
    ----------
    df : pandas.DataFrame
        Dataset with columns 'L', 'M', 'F'
    title : str, default='Saviesa Framework'
        Plot title
    save_path : str or None, default=None
        Path to save figure (if None, displays only)
    figsize : tuple, default=(10, 6)
        Figure size (width, height)
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
        
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'L': np.random.uniform(0.5, 1.0, 100),
    ...     'M': np.random.uniform(0.4, 0.9, 100)
    ... })
    >>> df['F'] = df['L'] * df['M']
    >>> fig = plot_scatter_LM(df, title='Example', 
    ...                       save_path='figures/example.png')
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots(figsize=figsize)
    scatter = ax.scatter(df['M'], df['L'], c=df['F'], 
                        cmap='viridis', s=100, alpha=0.7)
    plt.colorbar(scatter, ax=ax, label='Performance (F)')
    ax.set_xlabel('Milieu (M)', fontsize=12)
    ax.set_ylabel('Levier (L)', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
```

### plot_residuals

```python
def plot_residuals(y_true, y_pred, title='Residuals Plot',
                   save_path=None, figsize=(10, 6)):
    """
    Create residuals plot
    
    Parameters
    ----------
    y_true : array-like
        True values
    y_pred : array-like
        Predicted values
    title : str, default='Residuals Plot'
        Plot title
    save_path : str or None, default=None
        Path to save figure
    figsize : tuple, default=(10, 6)
        Figure size
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object
    """
    import matplotlib.pyplot as plt
    
    residuals = y_true - y_pred
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(y_pred, residuals, alpha=0.7)
    ax.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax.set_xlabel('Predicted Values', fontsize=12)
    ax.set_ylabel('Residuals', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
```

---

## 🛠️ Utils Module

**Location**: `scripts/utils/data_utils.py`

### normalize_01

```python
def normalize_01(series):
    """
    Normalize series to [0,1] range
    
    Parameters
    ----------
    series : pandas.Series or array-like
        Input data
        
    Returns
    -------
    normalized : pandas.Series or array
        Normalized data in [0,1]
        
    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.Series([10, 20, 30, 40, 50])
    >>> normalized = normalize_01(data)
    >>> print(normalized)
    0    0.00
    1    0.25
    2    0.50
    3    0.75
    4    1.00
    dtype: float64
    """
    return (series - series.min()) / (series.max() - series.min())
```

### load_dataset

```python
def load_dataset(dataset_name):
    """
    Load processed dataset
    
    Parameters
    ----------
    dataset_name : str
        Name of dataset ('covid' or 'education')
        
    Returns
    -------
    df : pandas.DataFrame
        Loaded dataset
        
    Examples
    --------
    >>> df_covid = load_dataset('covid')
    >>> print(df_covid.shape)
    (65, 8)
    """
    import pandas as pd
    
    if dataset_name.lower() == 'covid':
        path = 'data/processed/Article2_Dataset_COVID.csv'
    elif dataset_name.lower() == 'education':
        path = 'data/processed/Article2_Dataset_Education.csv'
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    return pd.read_csv(path)
```

---

## 📚 Complete Example

```python
# Import modules
from scripts.utils.models import MultiplicativeModel, AdditiveModel
from scripts.utils.metrics import compute_r2, identify_limiting_factors
from scripts.utils.visualization import plot_scatter_LM
from scripts.utils.data_utils import load_dataset
import numpy as np

# Load data
df = load_dataset('covid')

# Prepare features
X = df[['L', 'M']].values
y = df['F'].values

# Fit multiplicative model
model_mult = MultiplicativeModel()
model_mult.fit(X, y)
y_pred_mult = model_mult.predict(X)

# Fit additive model
model_add = AdditiveModel()
model_add.fit(X, y)
y_pred_add = model_add.predict(X)

# Compare models
r2_mult = compute_r2(y, y_pred_mult)
r2_add = compute_r2(y, y_pred_add)

print(f"R² (multiplicative): {r2_mult:.4f}")
print(f"R² (additive): {r2_add:.4f}")
print(f"Coefficients: β_L={model_mult.coef_[0]:.3f}, "
      f"β_M={model_mult.coef_[1]:.3f}")

# Identify limiting factors
df['limiting'] = identify_limiting_factors(df)
print(df['limiting'].value_counts())

# Visualize
fig = plot_scatter_LM(df, title='COVID-19 Validation',
                      save_path='figures/covid_scatter.png')
```

---

**Last updated**: January 2026  
**Version**: 1.0.0

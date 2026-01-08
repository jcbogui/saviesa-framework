# Running Validation Scripts

This tutorial explains how to run the validation scripts to test the Saviesa multiplicative model on empirical datasets.

---

## 📋 Overview

The Saviesa Framework includes two validation scripts:
1. **COVID-19 Validation**: Tests the model on vaccination data (n=65 departments)
2. **Education Validation**: Tests the model on lycée performance data (n=2,325 lycées)

---

## 🚀 Quick Start

### Run COVID-19 Validation

```bash
# From project root
python scripts/validation/validation_covid.py
```

**Expected output**:
```
✅ COVID-19 Validation Results
Sample size: n=65 departments
R² (multiplicative): 1.0000
R² (additive): 0.9951
Improvement: +0.49%
β_L: 1.000 (expected: 1.0)
β_M: 1.000 (expected: 1.0)
```

### Run Education Validation

```bash
# From project root
python scripts/validation/validation_education.py
```

**Expected output**:
```
✅ Education Validation Results
Sample size: n=2,325 lycées
R² (multiplicative): 0.4922
R² (additive): 0.4888
Improvement: +0.34%
β_O: 0.998
β_L: 0.997
β_M: 1.002
```

---

## 🔍 Understanding the Scripts

### COVID-19 Validation Script

**Location**: `scripts/validation/validation_covid.py`

**What it does**:
1. Loads processed COVID dataset
2. Fits multiplicative model: log(F) = β₀ + β_L·log(L) + β_M·log(M)
3. Fits additive model: F = β₀ + β_L·L + β_M·M
4. Compares R² values
5. Identifies limiting factors

**Key functions**:
```python
def load_covid_data():
    """Load and prepare COVID dataset"""
    df = pd.read_csv('data/processed/Article2_Dataset_COVID.csv')
    return df

def fit_multiplicative_model(df):
    """Fit log-linear multiplicative model"""
    X = np.log(df[['L', 'M']])
    y = np.log(df['F'])
    model = LinearRegression()
    model.fit(X, y)
    return model

def fit_additive_model(df):
    """Fit linear additive model"""
    X = df[['L', 'M']]
    y = df['F']
    model = LinearRegression()
    model.fit(X, y)
    return model
```

---

### Education Validation Script

**Location**: `scripts/validation/validation_education.py`

**What it does**:
1. Loads processed Education dataset
2. Fits multiplicative model: log(F) = β₀ + β_O·log(O) + β_L·log(L) + β_M·log(M)
3. Fits additive model: F = β₀ + β_O·O + β_L·L + β_M·M
4. Compares R² values
5. Analyzes ceiling effects

**Key difference**: Includes **O (Orientation)** variable for lycée type.

---

## 📊 Detailed Analysis

### Step 1: Load Data

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load COVID dataset
df = pd.read_csv('data/processed/Article2_Dataset_COVID.csv')

print(f"Sample size: n={len(df)}")
print(df[['L', 'M', 'F']].describe())
```

### Step 2: Fit Multiplicative Model

```python
# Log-linear regression
X = np.log(df[['L', 'M']])
y = np.log(df['F'])

model_mult = LinearRegression()
model_mult.fit(X, y)

# Display results
print(f"R² (multiplicative): {model_mult.score(X, y):.4f}")
print(f"β_L: {model_mult.coef_[0]:.3f}")
print(f"β_M: {model_mult.coef_[1]:.3f}")
print(f"β₀: {model_mult.intercept_:.3f}")
```

### Step 3: Fit Additive Model

```python
# Linear regression
X_add = df[['L', 'M']]
y_add = df['F']

model_add = LinearRegression()
model_add.fit(X_add, y_add)

# Display results
print(f"R² (additive): {model_add.score(X_add, y_add):.4f}")
```

### Step 4: Compare Models

```python
r2_mult = model_mult.score(X, y)
r2_add = model_add.score(X_add, y_add)

improvement = ((r2_mult - r2_add) / r2_add) * 100

print(f"\n📊 Model Comparison:")
print(f"R² (multiplicative): {r2_mult:.4f}")
print(f"R² (additive): {r2_add:.4f}")
print(f"Improvement: {improvement:+.2f}%")
```

### Step 5: Identify Limiting Factors

```python
# Determine which factor limits performance
df['limiting_factor'] = df.apply(
    lambda row: 'L' if row['L'] < row['M'] else 'M',
    axis=1
)

# Count
counts = df['limiting_factor'].value_counts()
print(f"\n🔍 Limiting Factors:")
print(f"M (Milieu) limiting: {counts.get('M', 0)} departments ({counts.get('M', 0)/len(df)*100:.1f}%)")
print(f"L (Levier) limiting: {counts.get('L', 0)} departments ({counts.get('L', 0)/len(df)*100:.1f}%)")
```

---

## 📈 Visualization

### Generate Scatter Plot

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['M'], df['L'], c=df['F'], 
                     cmap='viridis', s=100, alpha=0.7)
plt.colorbar(scatter, label='Performance (F)')
plt.xlabel('Milieu (M)', fontsize=12)
plt.ylabel('Levier (L)', fontsize=12)
plt.title('Saviesa Framework: COVID-19 Validation (n=65)', fontsize=14)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figures/covid_validation_scatter.png', dpi=300)
plt.show()
```

### Generate Residuals Plot

```python
# Predict with multiplicative model
y_pred = model_mult.predict(X)
residuals = y - y_pred

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.7)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted log(F)', fontsize=12)
plt.ylabel('Residuals', fontsize=12)
plt.title('Residuals Plot: Multiplicative Model', fontsize=14)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figures/covid_residuals.png', dpi=300)
plt.show()
```

---

## 🧪 Custom Validation

### Validate Your Own Dataset

```python
# Load your dataset
df_custom = pd.read_csv('data/processed/your_dataset.csv')

# Ensure variables are present
required_vars = ['L', 'M', 'F']
assert all(var in df_custom.columns for var in required_vars), \
    "Missing required variables"

# Fit multiplicative model
X = np.log(df_custom[['L', 'M']])
y = np.log(df_custom['F'])

model = LinearRegression()
model.fit(X, y)

# Display results
print(f"✅ Validation Results:")
print(f"Sample size: n={len(df_custom)}")
print(f"R² (multiplicative): {model.score(X, y):.4f}")
print(f"β_L: {model.coef_[0]:.3f} (expected: ~1.0)")
print(f"β_M: {model.coef_[1]:.3f} (expected: ~1.0)")
```

---

## 🔬 Advanced Analysis

### Robustness Tests

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='r2')

print(f"\n🔬 Cross-Validation Results:")
print(f"Mean R²: {scores.mean():.4f}")
print(f"Std R²: {scores.std():.4f}")
print(f"95% CI: [{scores.mean() - 1.96*scores.std():.4f}, "
      f"{scores.mean() + 1.96*scores.std():.4f}]")
```

### Bootstrap Confidence Intervals

```python
from scipy import stats

# Bootstrap coefficients
n_bootstrap = 1000
coef_L_bootstrap = []
coef_M_bootstrap = []

for _ in range(n_bootstrap):
    # Resample with replacement
    indices = np.random.choice(len(df), size=len(df), replace=True)
    df_boot = df.iloc[indices]
    
    # Fit model
    X_boot = np.log(df_boot[['L', 'M']])
    y_boot = np.log(df_boot['F'])
    model_boot = LinearRegression()
    model_boot.fit(X_boot, y_boot)
    
    coef_L_bootstrap.append(model_boot.coef_[0])
    coef_M_bootstrap.append(model_boot.coef_[1])

# Compute 95% CI
ci_L = np.percentile(coef_L_bootstrap, [2.5, 97.5])
ci_M = np.percentile(coef_M_bootstrap, [2.5, 97.5])

print(f"\n📊 Bootstrap 95% CI:")
print(f"β_L: [{ci_L[0]:.3f}, {ci_L[1]:.3f}]")
print(f"β_M: [{ci_M[0]:.3f}, {ci_M[1]:.3f}]")
```

---

## 📋 Validation Checklist

Before publishing your validation results:

- [ ] Sample size n ≥ 30
- [ ] All variables in [0,1] range
- [ ] No missing values
- [ ] Sufficient variability (CV > 5%)
- [ ] R² (multiplicative) ≥ R² (additive)
- [ ] Coefficients β_L, β_M ≈ 1.0 (±0.2)
- [ ] Residuals normally distributed
- [ ] Cross-validation performed
- [ ] Results documented

---

## 🆘 Troubleshooting

### Issue: RuntimeWarning: divide by zero in log
**Cause**: Variables contain zeros  
**Solution**: Add small constant (ε = 1e-6) before log transformation
```python
X = np.log(df[['L', 'M']] + 1e-6)
```

### Issue: Coefficients far from 1.0
**Cause**: Model may not be multiplicative, or data quality issues  
**Solution**: 
- Check data preparation steps
- Verify variable definitions
- Consider alternative models

### Issue: Low R²
**Cause**: High noise, missing variables, or non-multiplicative structure  
**Solution**:
- Add more explanatory variables
- Check for outliers
- Consider interaction terms

---

## 📚 Next Steps

1. **Methodology**: Understand the theoretical framework → [../methodology.md](../methodology.md)
2. **API Reference**: Explore available functions → [../api_reference.md](../api_reference.md)
3. **Examples**: See Jupyter notebooks → [../../examples/](../../examples/)

---

**Last updated**: January 2026  
**Version**: 1.0.0

# Data Preparation for Saviesa Framework

This tutorial explains how to prepare your own datasets for use with the Saviesa multiplicative performance model.

---

## 📋 Overview

The Saviesa Framework requires datasets with the following structure:
- **Performance variable (F)**: The outcome you want to model
- **Levier variable (L)**: Action/intervention factor [0,1]
- **Milieu variable (M)**: Context/environment factor [0,1]

Optional:
- **Orientation variable (O)**: Initial conditions [0,1]

---

## 🎯 Data Requirements

### Minimum Requirements
1. **Sample size**: n ≥ 30 observations (recommended: n ≥ 50)
2. **Variable range**: All variables should be normalized to [0,1]
3. **No missing values**: Complete data on L, M, F
4. **Variability**: Sufficient variance in L and M (CV > 5%)

### Recommended Structure

```csv
id,L,M,F
1,0.75,0.60,0.45
2,0.82,0.55,0.45
3,0.68,0.72,0.49
...
```

---

## 🔧 Step-by-Step Preparation

### Step 1: Load Raw Data

```python
import pandas as pd
import numpy as np

# Example: Load your raw data
df_raw = pd.read_csv('data/raw/your_dataset.csv')

print(f"Initial sample size: n={len(df_raw)}")
print(df_raw.head())
```

### Step 2: Handle Missing Values

```python
# Check missing values
print(df_raw.isnull().sum())

# Option A: Remove rows with missing values
df = df_raw.dropna(subset=['key_variable_1', 'key_variable_2'])

# Option B: Impute missing values (use with caution)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
df[['var1', 'var2']] = imputer.fit_transform(df[['var1', 'var2']])

print(f"Final sample size: n={len(df)}")
```

### Step 3: Normalize Variables to [0,1]

```python
def normalize_01(series):
    """Normalize a series to [0,1] range"""
    return (series - series.min()) / (series.max() - series.min())

# Example: Normalize raw variables
df['L'] = normalize_01(df['raw_action_variable'])
df['M'] = normalize_01(df['raw_context_variable'])

# Verify normalization
print(df[['L', 'M']].describe())
# Check: min should be 0.0, max should be 1.0
```

### Step 4: Compute Performance Variable

```python
# Option A: Direct measurement
df['F'] = normalize_01(df['raw_performance'])

# Option B: Composite index
# If F is a composite of multiple indicators
indicator1_norm = normalize_01(df['indicator1'])
indicator2_norm = normalize_01(df['indicator2'])
indicator3_norm = normalize_01(df['indicator3'])

df['F'] = (indicator1_norm + indicator2_norm + indicator3_norm) / 3

# Option C: Multiplicative construction (if testing the model)
df['F'] = df['L'] * df['M']
```

### Step 5: Create Composite Variables (if needed)

```python
# Example: M as composite of socioeconomic factors
income_norm = normalize_01(df['median_income'])
education_norm = normalize_01(df['education_index'])
health_norm = normalize_01(df['health_index'])

df['M'] = (income_norm + education_norm + health_norm) / 3

# Verify composite
print(f"M - Mean: {df['M'].mean():.3f}, SD: {df['M'].std():.3f}")
```

---

## 📊 Data Quality Checks

### Check 1: Variable Ranges

```python
# All variables should be in [0,1]
for var in ['L', 'M', 'F']:
    print(f"{var}: min={df[var].min():.3f}, max={df[var].max():.3f}")
    assert df[var].min() >= 0 and df[var].max() <= 1, f"{var} not in [0,1]"
```

### Check 2: Variability

```python
# Coefficient of variation (CV) should be > 5%
for var in ['L', 'M', 'F']:
    cv = (df[var].std() / df[var].mean()) * 100
    print(f"{var}: CV = {cv:.1f}%")
    if cv < 5:
        print(f"⚠️ Warning: {var} has low variability (CV < 5%)")
```

### Check 3: Correlations

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Correlation matrix
corr = df[['L', 'M', 'F']].corr()
print(corr)

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
            vmin=-1, vmax=1, square=True)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('figures/correlation_matrix.png', dpi=300)
plt.show()
```

### Check 4: Outliers

```python
# Identify potential outliers (values > 3 SD from mean)
for var in ['L', 'M', 'F']:
    mean = df[var].mean()
    std = df[var].std()
    outliers = df[(df[var] < mean - 3*std) | (df[var] > mean + 3*std)]
    print(f"{var}: {len(outliers)} potential outliers")
    if len(outliers) > 0:
        print(outliers[['id', var]])
```

---

## 💾 Save Processed Dataset

```python
# Select final columns
df_final = df[['id', 'L', 'M', 'F']].copy()

# Add metadata columns if available
if 'name' in df.columns:
    df_final.insert(1, 'name', df['name'])

# Save to processed folder
output_path = 'data/processed/your_dataset_processed.csv'
df_final.to_csv(output_path, index=False)

print(f"✅ Processed dataset saved: {output_path}")
print(f"Final sample size: n={len(df_final)}")
```

---

## 📝 Documentation Template

Create a README for your dataset:

```markdown
# Dataset: [Your Dataset Name]

**File**: `your_dataset_processed.csv`
**Sample size**: n=[number]
**Date**: [date]

## Variables

- **L (Levier)**: [Description of action/intervention variable]
  - Source: [data source]
  - Range: [0,1]
  - Mean: [value], SD: [value]

- **M (Milieu)**: [Description of context/environment variable]
  - Source: [data source]
  - Range: [0,1]
  - Mean: [value], SD: [value]

- **F (Performance)**: [Description of outcome variable]
  - Source: [data source]
  - Range: [0,1]
  - Mean: [value], SD: [value]

## Processing Steps

1. [Step 1]
2. [Step 2]
...

## Data Sources

- [Source 1]: [URL]
- [Source 2]: [URL]
```

---

## 🎯 Example: COVID-19 Dataset

See how the COVID-19 dataset was prepared:

```python
# Load raw VACSI data
df_vacsi = pd.read_csv('data/raw/covid_vaccination_data.csv', sep=';')

# Filter to metropolitan departments
df = df_vacsi[df_vacsi['dep'].str.match(r'^\d{2}$')].copy()

# Extract latest date
latest_date = df['jour'].max()
df = df[df['jour'] == latest_date]

# Create L (vaccination coverage)
df['L'] = df['couv_complet'] / 100

# Merge socioeconomic data for M
df_socio = pd.read_csv('data/raw/filosofi_2021_revenus.csv', sep=';')
df = df.merge(df_socio, left_on='dep', right_on='CODGEO')

# Create M (composite socioeconomic index)
# ... (see data/processed/README_PROCESSED_DATA.md for details)

# Save
df[['dep', 'L', 'M', 'F']].to_csv(
    'data/processed/Article2_Dataset_COVID.csv', 
    index=False
)
```

---

## 🆘 Common Issues

### Issue: Variables not in [0,1]
**Solution**: Use `normalize_01()` function or clip values:
```python
df['L'] = df['L'].clip(0, 1)
```

### Issue: High correlation between L and M
**Solution**: This may indicate multicollinearity. Consider:
- Using different variables
- Principal Component Analysis (PCA)
- Documenting the correlation in your analysis

### Issue: Low variability (CV < 5%)
**Solution**: 
- Check if variable is appropriate for your context
- Consider using a different sample or time period
- Document the ceiling/floor effect

---

## 📚 Next Steps

1. **Run Validation**: Test your prepared dataset → [03_running_validation.md](03_running_validation.md)
2. **Methodology**: Understand the theoretical framework → [../methodology.md](../methodology.md)
3. **API Reference**: Explore available functions → [../api_reference.md](../api_reference.md)

---

**Last updated**: January 2026  
**Version**: 1.0.0

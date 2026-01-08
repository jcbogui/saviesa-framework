# Getting Started with Saviesa Framework

This tutorial will guide you through the first steps of using the Saviesa Framework for multiplicative performance modeling.

---

## 📋 Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher
- pip package manager
- Basic knowledge of Python and data analysis

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/saviesa-framework.git
cd saviesa-framework
```

### 2. Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Quick Start Example

### Load and explore the COVID-19 dataset

```python
import pandas as pd
import numpy as np
from scripts.utils.models import MultiplicativeModel

# Load processed COVID dataset
df = pd.read_csv('data/processed/Article2_Dataset_COVID.csv')

# Display first rows
print(df.head())

# Check variables
print(df.columns)
# Expected: department_code, department_name, vaccination_rate, 
#           revenu_median_rfc, IPS_moyen, taux_reussite_moyen, L, M, F
```

### Compute Saviesa variables

```python
# L (Levier): Vaccination coverage normalized [0,1]
df['L'] = df['vaccination_rate'] / 100

# M (Milieu): Composite socioeconomic index
# Normalize each component
revenu_norm = (df['revenu_median_rfc'] - df['revenu_median_rfc'].min()) / \
              (df['revenu_median_rfc'].max() - df['revenu_median_rfc'].min())
ips_norm = (df['IPS_moyen'] - df['IPS_moyen'].min()) / \
           (df['IPS_moyen'].max() - df['IPS_moyen'].min())
bac_norm = (df['taux_reussite_moyen'] - df['taux_reussite_moyen'].min()) / \
           (df['taux_reussite_moyen'].max() - df['taux_reussite_moyen'].min())

# Composite M
df['M'] = (revenu_norm + ips_norm + bac_norm) / 3

# F (Performance): Multiplicative model
df['F'] = df['L'] * df['M']

print(df[['L', 'M', 'F']].describe())
```

### Fit multiplicative model

```python
from sklearn.linear_model import LinearRegression

# Log-linear regression: log(F) = β₀ + β_L·log(L) + β_M·log(M)
X = np.log(df[['L', 'M']])
y = np.log(df['F'])

model = LinearRegression()
model.fit(X, y)

# Display coefficients
print(f"β_L = {model.coef_[0]:.4f} (expected: 1.0)")
print(f"β_M = {model.coef_[1]:.4f} (expected: 1.0)")
print(f"R² = {model.score(X, y):.4f}")
```

---

## 📈 Visualization

```python
import matplotlib.pyplot as plt

# Scatter plot: L vs M
plt.figure(figsize=(10, 6))
plt.scatter(df['M'], df['L'], c=df['F'], cmap='viridis', s=100, alpha=0.7)
plt.colorbar(label='Performance (F)')
plt.xlabel('Milieu (M)')
plt.ylabel('Levier (L)')
plt.title('Saviesa Framework: COVID-19 Vaccination (n=65 departments)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('figures/covid_scatter_LM.png', dpi=300)
plt.show()
```

---

## 🔍 Identify Limiting Factors

```python
# Determine which factor limits performance
df['limiting_factor'] = df.apply(
    lambda row: 'L' if row['L'] < row['M'] else 'M', 
    axis=1
)

# Count limiting factors
print(df['limiting_factor'].value_counts())

# Departments where L is limiting
print("\nDepartments limited by L (vaccination):")
print(df[df['limiting_factor'] == 'L'][['department_name', 'L', 'M', 'F']])
```

---

## 📚 Next Steps

1. **Data Preparation**: Learn how to prepare your own datasets → [02_data_preparation.md](02_data_preparation.md)
2. **Running Validation**: Run full validation scripts → [03_running_validation.md](03_running_validation.md)
3. **Methodology**: Understand the theoretical framework → [../methodology.md](../methodology.md)

---

## 🆘 Troubleshooting

### Issue: Missing dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Import errors
Ensure you're in the project root directory and have activated your virtual environment.

### Issue: Data not found
Check that you're running scripts from the project root:
```bash
cd /path/to/saviesa-framework
python scripts/validation/validation_covid.py
```

---

## 📖 Additional Resources

- [Main README](../../README.md)
- [API Reference](../api_reference.md)
- [Examples Notebooks](../../examples/)

---

**Last updated**: January 2026  
**Version**: 1.0.0

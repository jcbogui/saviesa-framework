# Scripts Directory

Python scripts for Saviesa framework validation and analysis.

---

## 📂 Structure

```
scripts/
├── validation/         # Validation scripts
│   ├── validation_covid.py
│   ├── validation_education.py
│   ├── diagnostic_differentiel.py
│   └── loocv_validation.py
└── utils/              # Utility functions
    ├── models.py
    ├── metrics.py
    └── visualization.py
```

---

## 🚀 Usage

### **1. COVID-19 Validation**

```bash
python scripts/validation/validation_covid.py
```

**Output**:
- R² comparison (multiplicative vs additive)
- RMSE and MAE metrics
- Limiting factor distribution
- Results saved to `results/Validation_COVID_Results.csv`

---

### **2. Education Validation**

```bash
python scripts/validation/validation_education.py
```

**Output**:
- R² comparison (multiplicative vs additive)
- RMSE and MAE metrics
- Coefficient estimates
- Results saved to `results/Validation_Education_Results.csv`

---

### **3. Diagnostic Comparison**

```bash
python scripts/validation/diagnostic_differentiel.py
```

**Output**:
- Convergence vs divergence analysis
- Efficiency gain calculations
- Recommendation comparison table
- Results saved to `results/Diagnostic_Differentiel_Results.csv`

---

### **4. LOOCV Validation**

```bash
python scripts/validation/loocv_validation.py
```

**Output**:
- R² LOOCV for all models
- RMSE LOOCV
- AIC comparison
- Results saved to `results/LOOCV_Results.csv`

---

## 🔧 Utility Modules

### **models.py**

Model implementations:
- `fit_additive_model()`: Linear additive model
- `fit_interaction_model()`: Interaction model
- `fit_multiplicative_model()`: Log-linear multiplicative model
- `identify_limiting_factor()`: Find min(O, L, M)

### **metrics.py**

Performance metrics:
- `calculate_r2()`: R² coefficient
- `calculate_rmse()`: Root Mean Squared Error
- `calculate_mae()`: Mean Absolute Error
- `calculate_aic()`: Akaike Information Criterion

### **visualization.py**

Plotting functions:
- `plot_scatter()`: Observed vs predicted
- `plot_distribution()`: Limiting factor distribution
- `plot_heatmap()`: Geographic visualization
- `plot_comparison()`: Model comparison

---

## 📋 Requirements

All scripts require:
- Python 3.11+
- Dependencies from `requirements.txt`

Install:
```bash
pip install -r requirements.txt
```

---

## 📧 Questions?

Contact: [jean.bogui@proton.me](mailto:jean.bogui@proton.me)

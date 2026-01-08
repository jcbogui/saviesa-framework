# Saviesa Framework Methodology

This document presents the theoretical and methodological foundations of the Saviesa multiplicative performance model.

---

## 📋 Table of Contents

1. [Theoretical Framework](#theoretical-framework)
2. [Mathematical Model](#mathematical-model)
3. [Key Concepts](#key-concepts)
4. [Model Validation](#model-validation)
5. [Interpretation Guidelines](#interpretation-guidelines)
6. [Limitations](#limitations)

---

## 🎯 Theoretical Framework

### Core Principle

The Saviesa Framework models **institutional performance** as a **multiplicative function** of three factors:

**F = O × L × M**

Where:
- **F (Performance)**: Observed outcome or achievement
- **O (Orientation)**: Initial conditions or strategic positioning
- **L (Levier)**: Action, intervention, or leverage factor
- **M (Milieu)**: Context, environment, or structural conditions

### Non-Compensability

The multiplicative structure implies **non-compensability**: a low value in one factor cannot be fully compensated by high values in others. This reflects real-world constraints where:
- High action (L) cannot overcome adverse context (M)
- Favorable context (M) requires action (L) to materialize into performance

### Limiting Factor Principle

Performance is constrained by the **minimum factor**:
```
F_max = min(O, L, M)
```

This aligns with Liebig's Law of the Minimum in ecology and von Thünen's spatial economics.

---

## 📐 Mathematical Model

### Multiplicative Form

**Full model**:
```
F = O × L × M
```

**Simplified model** (when O is constant or absorbed):
```
F = L × M
```

### Log-Linear Transformation

Taking logarithms yields a linear model:
```
log(F) = log(O) + log(L) + log(M)
```

Or in regression form:
```
log(F) = β₀ + β_O·log(O) + β_L·log(L) + β_M·log(M) + ε
```

**Expected coefficients**: β_O ≈ β_L ≈ β_M ≈ 1.0

### Comparison with Additive Model

**Additive model**:
```
F = β₀ + β_L·L + β_M·M + ε
```

**Key difference**: Additive models assume compensability (high L can offset low M).

---

## 🔑 Key Concepts

### 1. Orientation (O)

**Definition**: Initial conditions, strategic positioning, or structural characteristics that shape the potential for performance.

**Examples**:
- **Education**: Type of lycée (General/Technological vs. Professional)
- **Healthcare**: Hospital category (University vs. Regional)
- **Business**: Industry sector or market position

**Range**: [0,1] normalized scale

**Interpretation**: O = 0.75 means the entity starts at 75% of maximum potential.

---

### 2. Levier (L)

**Definition**: Action, intervention, policy, or resource deployment that can be controlled or influenced.

**Examples**:
- **Education**: Teaching quality, pedagogical innovation
- **Healthcare**: Vaccination coverage, treatment protocols
- **Business**: Marketing investment, R&D spending

**Range**: [0,1] normalized scale

**Interpretation**: L = 0.80 means 80% of maximum action/intervention is deployed.

---

### 3. Milieu (M)

**Definition**: Context, environment, or structural conditions that are largely exogenous and difficult to change in the short term.

**Examples**:
- **Education**: Socioeconomic status (IPS), family background
- **Healthcare**: Population health status, infrastructure
- **Business**: Market conditions, regulatory environment

**Range**: [0,1] normalized scale

**Interpretation**: M = 0.60 means the context is at 60% of optimal conditions.

---

### 4. Performance (F)

**Definition**: Observed outcome, achievement, or effectiveness.

**Examples**:
- **Education**: Baccalauréat success rate, value-added
- **Healthcare**: Mortality rate, patient satisfaction
- **Business**: Profitability, market share

**Range**: [0,1] normalized scale

**Computation**: F = O × L × M (multiplicative) or measured directly

---

## ✅ Model Validation

### Validation Criteria

1. **Coefficient Test**: β_O, β_L, β_M ≈ 1.0 (±0.2)
2. **R² Comparison**: R²(multiplicative) ≥ R²(additive)
3. **Residuals**: Normally distributed, homoscedastic
4. **Cross-validation**: Stable coefficients across subsamples

### Empirical Evidence

**COVID-19 Validation (n=65 departments)**:
- R²(multiplicative) = 1.0000
- R²(additive) = 0.9951
- β_L = 1.000, β_M = 1.000
- **Conclusion**: Perfect multiplicative structure

**Education Validation (n=2,325 lycées)**:
- R²(multiplicative) = 0.4922
- R²(additive) = 0.4888
- β_O = 0.998, β_L = 0.997, β_M = 1.002
- **Conclusion**: Multiplicative structure confirmed, with ceiling effects

---

## 📊 Interpretation Guidelines

### Identifying Limiting Factors

```python
limiting_factor = min(O, L, M)
```

**Example**:
- O = 0.75, L = 0.85, M = 0.60
- Limiting factor: M (context)
- **Interpretation**: Performance is constrained by adverse context, not lack of action.

### Policy Implications

**If L is limiting**:
- Increase action/intervention
- Improve resource deployment
- Enhance policy effectiveness

**If M is limiting**:
- Address structural inequalities
- Improve contextual conditions
- Long-term investments in infrastructure

**If O is limiting**:
- Reconsider strategic positioning
- Adjust initial conditions
- Structural reforms

---

## 📈 Comparative Advantage

### vs. Additive Models

| Feature | Multiplicative | Additive |
|---------|----------------|----------|
| **Compensability** | No | Yes |
| **Limiting factors** | Explicit | Implicit |
| **Interpretation** | Intuitive | Complex |
| **Policy guidance** | Clear | Ambiguous |

### vs. Interaction Models

**Interaction model**: F = β₀ + β_L·L + β_M·M + β_LM·L×M

**Advantage of multiplicative**:
- Simpler structure (3 parameters vs. 4)
- Direct interpretation of coefficients
- No need to test interaction significance

---

## ⚠️ Limitations

### 1. Variable Selection

**Challenge**: Correctly identifying O, L, M requires domain expertise.

**Mitigation**: 
- Use theoretical frameworks
- Validate with experts
- Test alternative specifications

### 2. Normalization

**Challenge**: Normalizing to [0,1] may lose information.

**Mitigation**:
- Document normalization procedures
- Report raw statistics
- Test sensitivity to normalization method

### 3. Measurement Error

**Challenge**: Measurement error in log-transformed variables can bias coefficients.

**Mitigation**:
- Use reliable data sources
- Validate data quality
- Report confidence intervals

### 4. Ceiling/Floor Effects

**Challenge**: Variables near 0 or 1 may violate log-transformation assumptions.

**Mitigation**:
- Add small constant (ε = 1e-6) before log
- Document ceiling/floor effects
- Use alternative transformations if needed

### 5. Causality

**Challenge**: Multiplicative model does not imply causality.

**Mitigation**:
- Use causal inference methods (IV, RDD, etc.)
- Interpret as associations, not causal effects
- Conduct robustness tests

---

## 🔬 Extensions

### Time-Varying Models

```
F_t = O_t × L_t × M_t
```

Allows tracking performance evolution over time.

### Hierarchical Models

```
F_ij = O_j × L_ij × M_ij
```

Where i indexes individuals and j indexes groups (e.g., students in schools).

### Stochastic Models

```
F = O × L × M × exp(ε)
```

Where ε ~ N(0, σ²) captures random variation.

---

## 📚 References

### Theoretical Foundations

1. **Liebig's Law of the Minimum** (1840): Agricultural productivity limited by scarcest resource
2. **von Thünen's Spatial Economics** (1826): Location theory and multiplicative rent functions
3. **Cobb-Douglas Production Function** (1928): Multiplicative structure in economics

### Empirical Applications

1. **Bogui, J.C.** (2026). "Saviesa Framework: A Multiplicative Model of Institutional Performance". *Working Paper*.
2. **COVID-19 Validation**: Vaccination coverage and socioeconomic factors in French departments
3. **Education Validation**: Lycée performance and social position index (IPS)

---

## 📖 Further Reading

- [Getting Started Guide](tutorials/01_getting_started.md)
- [Data Preparation](tutorials/02_data_preparation.md)
- [Running Validation](tutorials/03_running_validation.md)
- [API Reference](api_reference.md)

---

**Last updated**: January 2026  
**Version**: 1.0.0  
**Author**: Jean Clément Bogui (ORCID: 0009-0006-9896-5653)

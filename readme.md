# ⚽ Football Analytics System  
## Match Outcome & Player Performance Prediction using Machine Learning

This project implements a **complete end-to-end football analytics pipeline**, starting from raw football data and ending with a **production-ready Streamlit application**.

It supports two predictive tasks:
- **Match Outcome Prediction** (Win / Draw / Loss) — Classification
- **Player Performance Prediction** (Score → Star Rating) — Regression

---

## 📌 Project Overview

- **Dataset:** Football match and player statistics (`2020-09-24.csv`)
- **Models Used:**
  - Gradient Boosting Classifier (Match Outcome)
  - Random Forest Regressor (Player Performance)
- **Frontend:** Streamlit
- **Core Focus:**
  - Data integrity
  - Feature engineering
  - Leakage prevention
  - Interpretability
  - Deployment-ready inference

---

# 🧠 Machine Learning Workflow  
## 20-Step Training & Evaluation Pipeline

---

### 1. Setup & Data Loading
- Imported core libraries: `pandas`, `matplotlib`, `scikit-learn`
- Loaded raw dataset: **2020-09-24.csv**

---

### 2. Initial Inspection
- Used `.shape`, `.info()`, `.describe()`
- Identified missing values and datatype issues

---

### 3. Role-Based Feature Categorization
- Grouped features by player role:
  - Goalkeeper
  - Defender
  - Midfielder
  - Attacker

---

### 4. Logic-Based Data Cleaning
- Dropped irrelevant identifiers (Name, Jersey Number)
- Resolved ambiguous `0` values based on player role

---

### 5. Exploratory Data Analysis (EDA)
- Visualized distributions and relationships
- Analyzed goals, shots, and match statistics

---

### 6. Feature Cleaning
- Converted percentage-based columns (e.g., Tackle success %) to numeric format

---

### 7. Feature Scaling
- Applied MinMaxScaler and StandardScaler
- Compared distributions before and after scaling

---

### 8. Target Engineering

**MatchOutcome (Classification):**
- Classes: Win, Draw, Loss

**PerformanceScore (Regression):**
- Engineered from normalized player statistics:
  - Assists
  - Tackles
  - Clearances
  - Saves
  - Clean Sheets

---

### 9. Role-Aware Imputation
- Non-role features set to `0`
- Role-specific features filled using role-based medians

---

### 10. Data Preparation
- Separated features (`X`) and targets (`y`)
- One-hot encoded categorical variables
- Encoded classification labels where required

---

### 11. Leakage Prevention
- Removed features directly contributing to target construction

---

### 12. Train–Test Split
- 80% training, 20% testing
- Applied separately for regression and classification

---

### 13. Final Imputation
- Used `SimpleImputer(strategy="median")`

---

### 14. Baseline Models
- Regression: Linear Regression
- Classification: Logistic Regression

---

### 15. Baseline Evaluation
- Regression: MAE, RMSE, R²
- Classification: Accuracy, Precision, Recall, F1-score

---

### 16. Advanced Models
- Regression: Random Forest Regressor
- Classification: Gradient Boosting Classifier

---

### 17. Hyperparameter Tuning
- Random Forest: GridSearchCV
- Gradient Boosting: RandomizedSearchCV

---

### 18. Feature Selection (Top 5)
- Selected top 5 most important features for each task
- Retrained optimized models using only these features

---

### 19. Model Serialization
- Saved final models and imputers using `joblib`

---

### 20. Inference Testing
- Reloaded saved models
- Tested on manually created edge cases

---

# 🚀 Streamlit Application — Inference Pipeline

---

## 🔹 Application Layout

📸 **Screenshot — App Layout**

![App Layout](screenshots/app_layout.png)

---

## 🔹 Match Outcome Prediction

**Input Features:**
- Shots (standardized)
- Passes
- Big chances created
- Yellow cards
- Red cards

**Output:**
- Win → Green success banner
- Draw → Blue info banner
- Loss → Red error banner

📸 **Screenshot — Match Outcome Prediction**

![Match Outcome Prediction](screenshots/match_outcome_prediction.png)

---

## 🔹 Player Performance Prediction

**Input Features:**
- Assists
- Tackles
- Clearances
- Saves
- Clean sheets

**Output:**
- Star rating (⭐ to ⭐⭐⭐⭐⭐)
- Qualitative label (Poor → Elite)
- Progress bar visualization

📸 **Screenshots**

![Application Interface](screenshots/match_outcome_prediction_page.png)
![Match Outcome Prediction](screenshots/match_outcome_prediction.png)
![Player Performance Prediction](screenshots/player_performance_prediction.png)

---


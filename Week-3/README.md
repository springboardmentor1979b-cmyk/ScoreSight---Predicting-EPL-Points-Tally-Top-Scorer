Here is a **separate README file for Week 3**, written in the **same professional internship-style format**, so you can place it inside a **`Week-3/` folder** on your GitHub repo.

You can save this as **`README.md`** inside `Week-3`.

---

# 📅 Week 3 – Feature Engineering & Scaling

**Project:** *ScoreSight – Predicting EPL Points Tally & Top Scorer*
**Internship:** Infosys Internship (AIML)

---

## 📌 Objective

The objective of **Week 3** is to prepare the cleaned dataset for machine learning by performing **feature engineering and feature scaling**.
This step ensures that all numerical features contribute equally during model training.

---

## 📂 Input Dataset

* **File Used:** `epl_players_cleaned.csv`
* **Source:** Output from Week 2 (Data Cleaning & Preprocessing)
* **Records:** 571 players
* **Features:** Numerical performance metrics and identifiers

---

## 🔧 Tasks Performed

### 1️⃣ Feature Selection

* Removed non-essential or identifier columns such as:

  * Player name
  * Team name
  * Index-like columns
* Retained **numerical performance-based features** relevant for prediction.

---

### 2️⃣ Feature Engineering

* Identified important features affecting:

  * Player performance
  * Goal scoring
  * Overall contribution to team points
* Ensured all selected features are numeric and ML-compatible.

---

### 3️⃣ Feature Scaling

Since ML models are sensitive to feature magnitude, scaling was applied.

#### 🔹 Min-Max Scaling

* Scales features between **0 and 1**
* Useful for distance-based algorithms

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(X)
```

---

#### 🔹 Standardization (Z-score Scaling)

* Mean = 0, Standard Deviation = 1
* Helps models converge faster

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(X)
```

---

### 4️⃣ Comparison of Scaled vs Unscaled Data

* Verified distribution before and after scaling
* Ensured no data leakage during transformation

---

## 💾 Output Files

* `minmax_scaled_data.csv`
* `standard_scaled_data.csv`

These datasets are used for **model training in Week 4**.

---

## 🛠 Tools & Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Google Colab

---

## 📈 Outcome

✔ Features are normalized and standardized
✔ Dataset is ML-ready
✔ Improved training stability and performance

---

## 🔜 Next Steps (Week 4)

* Model selection (Regression models)
* Training and testing split
* Performance evaluation (RMSE, MAE, R²)

---

## 👩‍💻 Author

**Tanisha Bhowmik**
AIML Intern – Infosys
*ScoreSight Project*

---

If you want, I can also:

* ✔ Create **Week-4 README**
* ✔ Create a **main README that links Week 1–Week 4**
* ✔ Help you **organize folders correctly in GitHub**
* ✔ Write **commit messages** for each week

Just say the word 🚀

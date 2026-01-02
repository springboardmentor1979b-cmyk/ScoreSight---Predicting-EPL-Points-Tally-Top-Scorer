

# 📅 Week 2 – Data Cleaning & Preprocessing
---

## 📌 Objective

The goal of **Week 2** is to clean and preprocess the raw EPL player dataset to make it suitable for analysis and machine learning models.

This week focuses on:

* Handling missing values
* Treating unrealistic values (e.g., zeros)
* Ensuring data consistency
* Preparing a cleaned dataset for future weeks

---

## 📂 Dataset Information

* **File name:** `dataset - 2020-09-24.csv`
* **Source:** Google Drive (Infosys Internship folder)
* **Records:** 571 players
* **Features:** 59 columns (player stats, performance metrics, identifiers)

---

## 🧹 Data Cleaning Steps Performed

### 1️⃣ Missing Value Analysis

* Checked missing values using:

  ```python
  df.isnull().sum()
  ```
* Identified columns with high missing counts such as:

  * Goals per match
  * Shots
  * Assists
  * Tackles
  * Goalkeeping statistics

---

### 2️⃣ Handling Zeros as Missing Values

For performance-related numerical columns, **0 values were treated as missing** where unrealistic.

**Columns cleaned:**

* Goals
* Assists
* Appearances
* Shots
* Passes

**Approach:**

* Replace `0` with `NaN`
* Fill missing values using the **column mean**

---

### 3️⃣ Mean Imputation

```python
mean_val = df[col].replace(0, np.nan).mean()
df[col] = df[col].replace(0, np.nan)
df[col].fillna(mean_val)
```

This ensures:

* No loss of data
* Statistical consistency
* Readiness for ML models

---

### 4️⃣ Post-Cleaning Validation

* Verified that important columns contain **no missing values**
* Rechecked dataset shape and data types

---

## 💾 Output

* Cleaned dataset saved as:

  ```
  epl_players_cleaned.csv
  ```
* This cleaned dataset is used in **Week 3 onwards**

---

## 🛠 Tools & Libraries Used

* Python
* Pandas
* NumPy
* Google Colab
* Google Drive integration

---

## 📈 Outcome

✔ Dataset is clean and consistent
✔ Missing values handled logically
✔ Ready for feature scaling and modeling

---


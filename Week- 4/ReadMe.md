

# 📅 Week 4 – EPL Player Stats Scaling & Visualization

## 📂 Files Included

* **`dataset - 2020-09-24.csv`**
  Raw EPL player dataset stored in Google Drive.

* **`minmax_scaled_epl.csv`**
  Dataset scaled using **Min-Max Scaler** (range: 0–1).

* **`standard_scaled_epl.csv`**
  Dataset scaled using **Standard Scaler** (mean = 0, std = 1).

---

## 🎯 Objectives

The main objectives of Week 4 were to **prepare the EPL player dataset for modeling** by scaling numerical features and visualizing the effects of scaling.

* **Load** the EPL player dataset from Google Drive.
* **Check and handle missing values** in key numerical columns:

  * **Appearances**
  * **Passes**
* **Apply Min-Max Scaling** to normalize feature ranges (0–1).
* **Apply Standard Scaling** to standardize features (mean = 0, variance = 1).
* **Visualize relationships** between **Appearances** and **Goals**:

  * **Before scaling**
  * **After Min-Max scaling**

---

## 🛠️ Methods Used

### **Min-Max Scaling**

* Scales features between **0 and 1**.
* Useful when features have **different ranges**.
* Preserves the relative distribution of values while normalizing magnitude.

### **Standard Scaling**

* Centers data around **mean = 0**.
* Scales data to **unit variance** (standard deviation = 1).
* Suitable for algorithms like **Linear Regression, SVM, KNN**.

---

## 📊 Visualization

* Scatter plots were created to observe the **impact of scaling**:

  * **Before Scaling:** Raw data distribution
  * **After Scaling:** Normalized or standardized feature distribution

* These visualizations help verify that **scaling preserves relationships** between variables while standardizing magnitudes.

---

## ✅ Outcome

* Numerical features were **scaled successfully**.
* Data distributions were **normalized and standardized**.
* Visual confirmation of scaling effects was obtained.
* Scaled datasets are **ready for Week 5 – Model Building**.

---

## 🧰 Tools & Libraries

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Google Colab & Google Drive**


Do you want me to do that next?

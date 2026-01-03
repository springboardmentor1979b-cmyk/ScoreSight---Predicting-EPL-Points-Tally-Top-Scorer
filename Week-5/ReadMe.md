

# 📘 Week 5 – Model Training & Evaluation

## 📌 Overview

In **Week 5**, the goal was to apply **basic Machine Learning algorithms** on the pre-processed **English Premier League (EPL) player dataset**.
The dataset used this week was already **cleaned, encoded, and scaled** in the previous weeks.

Two types of models were built:

* **Regression Model** – to predict the number of goals scored by a player
* **Classification Model** – to predict the match result (**Win / Draw / Loss**)

This week focused on understanding how **machine learning models are trained, tested, evaluated, and visualized**.

---

## 📌 Dataset

* **Location:** `../Week-4_Feature_Scaling/minmax_scaled_epl.csv`
* **Dataset Name:** EPL Players Dataset
* **Source:** Google Drive (provided during internship)

### **Preprocessing Status**

* Missing values handled
* Categorical variables encoded
* Numerical features scaled using **Min-Max Scaling**

---

## 🔹 Part 1: Regression Model (Goals Prediction)

### 🧠 Problem Statement

Predict the **number of goals** scored by a player based on:

* **Appearances**
* **Shots**
* **Passes**
* **Assists**

### 🔧 Steps Followed

1. **Feature Selection**

   * **X (features):** `['Appearances', 'Shots', 'Passes', 'Assists']`
   * **y (target):** `'Goals'`

2. **Train-Test Split**

   * 80% data → Training
   * 20% data → Testing

3. **Model Used**

   * **Linear Regression**

4. **Evaluation Metrics**

   * **Mean Absolute Error (MAE)**
   * **Root Mean Squared Error (RMSE)**
   * **R² Score**

### 📈 Visualization

* Scatter plot of **Actual Goals vs Predicted Goals**
* Helps understand how well the model is performing

---

## 🔹 Part 2: Classification Model (Match Outcome Prediction)

### 🧠 Problem Statement

Classify the **match outcome** based on player statistics.

**Match Result Labels:**

* 0 → Loss
* 1 → Draw
* 2 → Win

### 🔧 Steps Followed

1. **Created a New Target Column**

   * `Match_Result` based on Wins and Losses

2. **Feature Selection**

   * **X (features):** `['Shots', 'Passes', 'Assists']`
   * **y (target):** `Match_Result`

3. **Model Used**

   * **Logistic Regression**

4. **Evaluation Metric**

   * **Accuracy Score**

### 📊 Visualization

* **Confusion Matrix**
* Shows how many predictions were correct or incorrect for each class

---

## 🧪 Model Results Summary

| Model Type     | Algorithm           | Evaluation Metrics         |
| -------------- | ------------------- | -------------------------- |
| Regression     | Linear Regression   | MAE, RMSE, R²              |
| Classification | Logistic Regression | Accuracy, Confusion Matrix |

---

## 🛠 Libraries Used

* **pandas**
* **matplotlib**
* **scikit-learn**

---

## ✅ Conclusion

Week 5 successfully demonstrated the **practical implementation of machine learning models** using real-world sports data.

* The **trained models provided reasonable predictions**.
* This week helped in understanding the **complete model training workflow** from feature selection to evaluation and visualization.

---

Do you want me to do that?

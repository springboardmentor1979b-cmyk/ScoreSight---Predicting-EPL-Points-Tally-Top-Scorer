# ⚽ ScoreSight EPL: Prediction System

*An end-to-end Machine Learning solution developed during my Data Science Internship to analyze English Premier League (EPL) performance.*

---

## 📌 Project Overview
**ScoreSight EPL** is a dual-purpose analytics platform that leverages Machine Learning to provide data-driven insights into football. The application features two distinct modules:
1.  **Match Outcome Predictor:** Analyzes match-day statistics to estimate the probability of a Win, Draw, or Loss.
2.  **Player Performance Predictor:** Utilizes historical career data to forecast a player's total goal-scoring impact.

---

## 🖼️ Application Preview

### 1. Player Performance Analytics
This screen allows users to simulate a player's career trajectory by adjusting key performance indicators such as appearances, shots, and passes.
<img width="1916" height="944" alt="Screenshot 2026-01-12 130557" src="https://github.com/user-attachments/assets/1cf9fe2d-8268-48b5-901d-2333113b95ae" />


### 2. Match Outcome Prediction
This screen translates tactical match-day stats into a predicted match result (Win/Draw/Loss) based on the model's impact scoring.
<img width="1914" height="938" alt="Screenshot 2026-01-12 130155" src="https://github.com/user-attachments/assets/33350672-8d17-42f3-bf55-56ce54ef990b" />

---

## 🧠 Technical Architecture

### **Data Pipeline**
- **Preprocessing:** - Feature scaling using `MinMaxScaler` to normalize data ranges.
    - Strict feature alignment to ensure model input consistency between training and real-time inference.

### **Machine Learning Models**
- **Algorithm:** Random Forest Regressor.
- **Why Random Forest?** It effectively captures non-linear relationships and interactions between variables (e.g., how the value of a 'Shot' increases when combined with high 'Pass' volume).
- **Target Variable:** Actual Career Goals ($y$).

### **Mathematical Logic**
- **Goal Prediction:** Derived directly from the trained regressor.
- **Assist Estimation:** Calculated using a domain-specific coefficient of **0.35**, representing the average assist-to-goal ratio for high-impact EPL attackers.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python |
| **Data Manipulation** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn |
| **Model Persistence** | Joblib |
| **Web Framework** | Streamlit |

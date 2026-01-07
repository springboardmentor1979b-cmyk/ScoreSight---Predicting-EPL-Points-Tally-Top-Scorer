import streamlit as st
import joblib
import numpy as np

# ---------------- LOAD MODELS ----------------
reg_model = joblib.load("C:/B.E. AIML/ScoreSight/models/linear_regression_model.pkl")
clf_model = joblib.load("C:/B.E. AIML/ScoreSight/models/xgb_classification_model.pkl")

# ---------------- APP TITLE ----------------
st.set_page_config(page_title="ScoreSight", layout="centered")
st.title("⚽ ScoreSight – EPL Prediction System")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Select Prediction Type",
    ["Player Performance Prediction", "Match Outcome Prediction"]
)

# ======================================================
# SCREEN 1: PLAYER PERFORMANCE (LINEAR REGRESSION)
# ======================================================
if menu == "Player Performance Prediction":

    st.header("📊 Player Performance Prediction (Goals)")

    st.write("Enter player statistics to predict goals scored:")

    # ---- INPUT FEATURES (must match training order) ----
    age = st.slider("Age", 16, 40, 25)
    appearances = st.slider("Appearances", 0, 50, 25)
    shots = st.slider("Shots", 0, 200, 30)
    passes = st.slider("Passes", 0, 3000, 500)

    if st.button("Predict Goals"):
        input_data = np.array([[age, appearances, shots, passes]])
        predicted_goals = reg_model.predict(input_data)[0]

        st.success(f"⚽ Predicted Goals: {predicted_goals:.2f}")

# ======================================================
# SCREEN 2: MATCH OUTCOME (XGBOOST CLASSIFICATION)
# ======================================================
if menu == "Match Outcome Prediction":

    st.header("🏟️ Match Outcome Prediction (Win / Draw / Loss)")

    st.write("Enter match-level features:")

    # ---- INPUT FEATURES (must match training order) ----
    home_team_strength = st.slider("Home Team Strength", 1, 100, 70)
    away_team_strength = st.slider("Away Team Strength", 1, 100, 65)
    home_form = st.slider("Home Team Recent Form", 0, 10, 6)
    away_form = st.slider("Away Team Recent Form", 0, 10, 5)

    if st.button("Predict Match Outcome"):
        input_data = np.array([[home_team_strength, away_team_strength,
                                home_form, away_form]])

        prediction = clf_model.predict(input_data)[0]

        outcome_map = {
            2: "🏠 Home Win",
            1: "🤝 Draw",
            0: "🚗 Away Win"
        }

        st.success(f"Predicted Outcome: {outcome_map[prediction]}")

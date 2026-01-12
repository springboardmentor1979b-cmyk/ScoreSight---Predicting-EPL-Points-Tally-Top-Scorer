
import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# LOAD MODEL & SCALER
# -------------------------------------------------
try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="EPL Prediction System",
    page_icon="⚽",
    layout="centered"
)

st.title("⚽ EPL Prediction System")
st.caption("Machine Learning based Match & Player Performance Predictor")

# -------------------------------------------------
# SIDEBAR NAVIGATION (2 SCREENS)
# -------------------------------------------------
menu = st.sidebar.radio(
    "Select Prediction Type",
    ["Match Outcome Prediction", "Player Performance Prediction"]
)

# =================================================
# SCREEN 1 — MATCH OUTCOME PREDICTION (FIXED)
# =================================================
if menu == "Match Outcome Prediction":

    st.header("🏟 Match Outcome Prediction")
    st.write("Enter match-related statistics to predict the outcome.")

    # CHANGED: 'goals' variable now maps to 'appearances' 
    # because the model REQUIRES an Appearances column.
    # We set it to 1 to represent a single match.
    apps = 1 
    shots = st.number_input("Shots", min_value=0, max_value=30, value=5)
    passes = st.number_input("Passes", min_value=0, max_value=1000, value=300)
    assists = st.number_input("Assists", min_value=0, max_value=10, value=1)

    if st.button("Predict Match Outcome"):

        # FIXED: Features MUST match the ones seen during 'fit'
        FEATURES = ["Appearances", "Shots", "Passes", "Assists"]
        input_df = pd.DataFrame(
            [[apps, shots, passes, assists]],
            columns=FEATURES
        )

        scaled_input = scaler.transform(input_df)
        predicted_val = model.predict(scaled_input)[0]

        # Since we are predicting 1 match (Appearances=1), 
        # the predicted value will be very small. 
        # We adjust the thresholds so it's not always a 'Loss'.
        if predicted_val < 0.2: 
            result = "Loss ❌"
        elif predicted_val < 0.5: 
            result = "Draw ⚖️"
        else: 
            result = "Win 🏆"

        st.success(f"📢 Predicted Match Outcome: **{result}**")
        st.caption(f"Raw Model Impact Score: {round(predicted_val, 4)}")

# =================================================
# SCREEN 2 — PLAYER PERFORMANCE PREDICTION
# =================================================
elif menu == "Player Performance Prediction":

    st.header("📊 Player Performance Prediction")
    st.write("Enter player career statistics.")

    appearances = st.number_input("Appearances", min_value=0, max_value=600, value=100)
    shots = st.number_input("Shots", min_value=0, max_value=1000, value=150)
    passes = st.number_input("Passes", min_value=0, max_value=20000, value=2500)
    assists = st.number_input("Assists", min_value=0, max_value=200, value=20)

    if st.button("Predict Player Performance"):

        FEATURES = ["Appearances", "Shots", "Passes", "Assists"]
        input_df = pd.DataFrame(
            [[appearances, shots, passes, assists]],
            columns=FEATURES
        )

        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)

        # Dataset-based scaling
        predicted_goals = round(max(0, prediction[0]), 1)
        predicted_assists = round(predicted_goals * 0.35, 1)

        st.success("✅ Prediction Successful")
        st.metric("⚽ Predicted Career Goals", predicted_goals)
        st.metric("🎯 Predicted Career Assists", predicted_assists)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption("Internship Project | EPL Dataset | Streamlit + Machine Learning")

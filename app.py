import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- LOAD MODELS ----------------
with open("player_performance_model.pkl", "rb") as f:
    player_model = pickle.load(f)

with open("match_outcome_model.pkl", "rb") as f:
    match_model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EPL Prediction App",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* App background */
.stApp {
    background: linear-gradient(180deg, #0f172a 0%, #020617 100%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Card container */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 32px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.45);
    animation: fadeIn 0.8s ease-in-out;
}

/* Card title (Match Outcome / Player Performance) */
.title {
    text-align: center;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 20px;
    letter-spacing: 0.5px;
}

/* Input labels (Home Goals, Assists, etc.) */
label, .stNumberInput label, .stSlider label {
    color: white !important;
    font-weight: 500;
    font-size: 15px;
}

/* Inputs */
input, .stNumberInput input {
    background-color: #020617 !important;
    color: #ffffff !important;
    border-radius: 8px;
}

/* Slider text */
.stSlider span {
    color: #000000 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #1e40af);
    color: white;
    border: none;
    padding: 12px 22px;
    font-size: 15px;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #1e3a8a);
    transform: scale(1.03);
}

/* Success box */
.stAlert {
    background-color: rgba(16, 185, 129, 0.15);
    color: #ffffff;
    border-radius: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #e5e7eb;
    font-size: 14px;
    margin-top: 40px;
}

/* Smooth slide-in animation for screens */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Apply animation to cards */
.card {
    animation: slideIn 0.6s ease-in-out;
}

/* Streamlit button hover animation */
.stButton > button {
    transition: all 0.3s ease-in-out;
    background: linear-gradient(135deg, #5b21b6, #22c55e);
    color: white;
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    transform: scale(1.06);
    box-shadow: 0 0 14px rgba(34, 197, 94, 0.9);
}


label { color: white !important; }
            
section[data-testid="stSidebar"] label {
    color: black !important;
}


</style>
""", unsafe_allow_html=True)




# ---------------- SIDEBAR ----------------
st.sidebar.title("⚽ EPL Predictor")
page = st.sidebar.radio(
    "Choose Prediction Type:",
    ["Match Outcome", "Player Performance"]
)

# ================= SCREEN 1 =================
if page == "Match Outcome":

    st.markdown("<div class='title'>📊 Match Outcome Prediction</div>", unsafe_allow_html=True)


    home_goals = st.number_input("Home Goals", min_value=0, step=1)
    away_goals = st.number_input("Away Goals", min_value=0, step=1)
    shots_on_target = st.number_input("Shots on Target", min_value=0)
    possession = st.slider("Possession (%)", 0, 100, 50)

    if st.button("Predict Match Result"):
        input_data = np.array([[home_goals, away_goals, shots_on_target]])
        prediction = match_model.predict(input_data)[0]

        result_map = {2: "🏆 Win", 1: "🤝 Draw", 0: "❌ Loss"}
        st.markdown(
    f"""
    <h3 class='fade-in' style='color:#22c55e; text-align:center;'>
        Predicted Outcome: {result_map[prediction]}
    </h3>
    """,
    unsafe_allow_html=True
)


# ================= SCREEN 2 =================
else:

    st.markdown("<div class='title'>🎯 Player Performance Prediction</div>", unsafe_allow_html=True)

    assists = st.number_input("Assists", min_value=0, step=1)
    shots = st.number_input("Shots", min_value=0, step=1)
    appearances = st.number_input("Appearances", min_value=1, step=1)

    if st.button("Predict Goals"):
        input_data = pd.DataFrame(
            [[assists, shots, appearances]],
            columns=["Assists", "Shots", "Appearances"]
        )
        goals_pred = player_model.predict(input_data)[0]
        st.markdown(
    f"""
    <h3 class='fade-in' style='color:#00ff9c; text-align:center;'>
        ⚽ Predicted Goals: {round(goals_pred, 2)}
    </h3>
    """,
    unsafe_allow_html=True)



# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>EPL Analytics Project</div>",
    unsafe_allow_html=True
)

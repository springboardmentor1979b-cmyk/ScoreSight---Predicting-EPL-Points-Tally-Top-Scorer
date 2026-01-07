import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="⚽ EPL Prediction App",
    layout="wide",
    page_icon="🏟️"
)

# ======================================================
# STRONG CONTRAST UI STYLING
# ======================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020024, #090979, #020024);
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* Headings */
h1, h2, h3, h4 {
    color: #facc15 !important;
}

/* Labels */
label {
    color: #e0f2fe !important;
    font-weight: 600;
}

/* Tabs */
.stTabs [role="tab"] {
    color: #e0e7ff !important;
    font-size: 16px;
}
.stTabs [aria-selected="true"] {
    color: #22d3ee !important;
    font-weight: bold;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.12);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}

/* Inputs */
input, textarea {
    background-color: #020617 !important;
    color: #ffffff !important;
    border-radius: 10px;
}

/* Slider numbers */
.stSlider span {
    color: #ffffff !important;
}

/* Buttons */
.stButton button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    border-radius: 14px;
    padding: 10px 25px;
}
.stButton button:hover {
    background: linear-gradient(135deg, #4ade80, #22c55e);
    box-shadow: 0 0 15px #22c55e;
}

/* Results */
.result {
    font-size: 26px;
    font-weight: 800;
    color: #4ade80;
    margin-top: 20px;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #c7d2fe;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================
st.markdown("<h1 style='text-align:center;'>⚽ EPL Prediction Application</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:#7dd3fc;'>Match Outcome & Player Performance Prediction</h4>", unsafe_allow_html=True)

# ======================================================
# CREATE MODELS (NO PKL FILES)
# ======================================================

# Match Outcome Model
match_df = pd.DataFrame({
    "HomeGoals": [2,1,3,0,2,1,4],
    "AwayGoals": [1,1,0,2,2,3,1],
    "ShotsOnTarget": [6,4,8,3,5,7,9],
    "Possession": [55,48,62,45,50,52,65],
    "Result": [2,1,2,0,1,0,2]
})

X_match = match_df.drop("Result", axis=1)
y_match = match_df["Result"]

match_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
match_pipeline.fit(X_match, y_match)

# Player Performance Model
player_df = pd.DataFrame({
    "Appearances": [10,20,15,25,18,30,22],
    "Shots": [20,40,25,50,30,60,45],
    "Passes": [300,700,450,800,500,900,650],
    "Goals": [5,10,7,15,8,18,12],
    "Assists": [2,6,4,8,5,10,7]
})

X_player = player_df[["Appearances", "Shots", "Passes"]]
y_player = player_df[["Goals", "Assists"]]

player_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
player_pipeline.fit(X_player, y_player)

# ======================================================
# TABS (2 SCREENS)
# ======================================================
tab1, tab2 = st.tabs(["🏟 Match Outcome", "👤 Player Performance"])

# ======================================================
# SCREEN 1
# ======================================================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Match Outcome Prediction")

    c1, c2 = st.columns(2)
    with c1:
        home_goals = st.number_input("Home Goals", min_value=0)
        possession = st.slider("Home Possession (%)", 0, 100, 50)
    with c2:
        away_goals = st.number_input("Away Goals", min_value=0)
        shots = st.number_input("Shots on Target", min_value=0)

    if st.button("Predict Match Outcome"):
        df = pd.DataFrame([{
            "HomeGoals": home_goals,
            "AwayGoals": away_goals,
            "ShotsOnTarget": shots,
            "Possession": possession
        }])
        pred = match_pipeline.predict(df)[0]
        result = {2:"🏆 WIN",1:"🤝 DRAW",0:"❌ LOSS"}
        st.markdown(f"<div class='result'>Predicted Result: {result[pred]}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# SCREEN 2
# ======================================================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Player Performance Prediction")

    c1, c2, c3 = st.columns(3)
    with c1:
        apps = st.number_input("Appearances", min_value=1)
    with c2:
        shots = st.number_input("Shots", min_value=0)
    with c3:
        passes = st.number_input("Passes", min_value=0)

    if st.button("Predict Player Performance"):
        df = pd.DataFrame([{
            "Appearances": apps,
            "Shots": shots,
            "Passes": passes
        }])
        goals, assists = player_pipeline.predict(df)[0]
        st.markdown(f"<div class='result'>⚽ Goals: {goals:.2f}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result'>🎯 Assists: {assists:.2f}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("<div class='footer'>EPL Analytics Mini Project © 2025</div>", unsafe_allow_html=True)

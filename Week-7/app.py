import streamlit as st
import joblib
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI ScoreSight – EPL Predictor",
    page_icon="⚽",
    layout="centered"
)

# ---------------- Load Models ----------------
rf_model = joblib.load("models/rf_regression_model.pkl")
gb_model = joblib.load("models/gb_classification_model.pkl")



# ---------------- Header ----------------
st.markdown(
    """
    <h1 style="text-align:center;">⚽ AI ScoreSight</h1>
    <h4 style="text-align:center;">EPL Match Outcome & Player Performance Predictor</h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- Sidebar ----------------
st.sidebar.title("📊 AI ScoreSight")
st.sidebar.markdown("### Internship Project")
st.sidebar.info(
    """
    **Features:**
    - Player Goals Prediction  
    - Match Outcome Prediction  

    **Tech Stack:**
    - Python
    - Machine Learning
    - Streamlit
    """
)

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 Developed as a 2-Month Internship Project")

# ---------------- Tabs ----------------
tab1, tab2 = st.tabs(["🎯 Player Performance", "🏆 Match Outcome"])

# ======================================================
# 🎯 TAB 1: PLAYER PERFORMANCE
# ======================================================
with tab1:
    st.subheader("Player Performance Prediction (Goals)")

    st.write("Enter player statistics to predict expected goals.")

    col1, col2 = st.columns(2)

    with col1:
        appearances = st.number_input(
            "Appearances", min_value=0, help="Number of matches played"
        )
        shots = st.number_input(
            "Shots", min_value=0, help="Total shots taken by the player"
        )

    with col2:
        passes = st.number_input(
            "Passes", min_value=0, help="Total passes made"
        )
        assists = st.number_input(
            "Assists", min_value=0, help="Number of assists"
        )

    if st.button("🔍 Predict Goals"):
        input_data = np.array([[appearances, shots, passes, assists]])
        prediction = rf_model.predict(input_data)

        st.success("Prediction Successful ✅")
        st.metric(
            label="⚽ Predicted Goals",
            value=f"{prediction[0]:.2f}"
        )

    with st.expander("ℹ How this prediction works"):
        st.write(
            "A Random Forest Regression model trained on historical EPL player "
            "performance data is used to predict expected goals."
        )

# ======================================================
# 🏆 TAB 2: MATCH OUTCOME
# ======================================================
with tab2:
    st.subheader("Match Outcome Prediction")

    st.write("Enter match-related statistics to predict the outcome.")

    col1, col2, col3 = st.columns(3)

    with col1:
        shots_m = st.number_input(
            "Shots", min_value=0, help="Total shots in the match"
        )
    with col2:
        passes_m = st.number_input(
            "Passes", min_value=0, help="Total passes in the match"
        )
    with col3:
        assists_m = st.number_input(
            "Assists", min_value=0, help="Total assists in the match"
        )

    if st.button("🔮 Predict Match Result"):
        input_data = np.array([[shots_m, passes_m, assists_m]])
        result = gb_model.predict(input_data)[0]

        if result == 2:
            st.success("🏆 Predicted Result: **Win**")
        elif result == 1:
            st.warning("🤝 Predicted Result: **Draw**")
        else:
            st.error("❌ Predicted Result: **Loss**")

    with st.expander("ℹ Model Details"):
        st.write(
            "A Gradient Boosting Classification model predicts match outcomes "
            "based on historical performance patterns."
        )

# ---------------- Footer ----------------
st.markdown(
    """
    <hr>
    <p style="text-align:center;">
    ⚽ AI ScoreSight | EPL Analytics System <br>
    Built using Machine Learning & Streamlit
    </p>
    """,
    unsafe_allow_html=True
)

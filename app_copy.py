import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Load Models & Imputers
# --------------------------------------------------
clf_model = joblib.load("top5_gradient_boosting_classifier.pkl")
reg_model = joblib.load("top5_random_forest_regressor.pkl")

clf_imputer = joblib.load("top5_classification_imputer.pkl")
reg_imputer = joblib.load("top5_regression_imputer.pkl")

# --------------------------------------------------
# Observed performance score range
# --------------------------------------------------
OBSERVED_MAX = 2.55

# --------------------------------------------------
# Strict feature alignment
# --------------------------------------------------
def strict_align_features(input_df, feature_names, defaults=None):
    aligned_df = pd.DataFrame(0, index=[0], columns=feature_names)

    if defaults:
        for col, val in defaults.items():
            if col in feature_names:
                aligned_df[col] = val

    for col in input_df.columns:
        if col in feature_names:
            aligned_df[col] = input_df[col].values

    return aligned_df

# --------------------------------------------------
# Navigation callbacks (CRITICAL FIX)
# --------------------------------------------------
def go_match():
    st.session_state.page = "match"

def go_player():
    st.session_state.page = "player"

# --------------------------------------------------
# App Config
# --------------------------------------------------
st.set_page_config(page_title="Football Analytics App", layout="centered")
st.title("⚽ Football Analytics Application")

# --------------------------------------------------
# Session State (DEFAULT PAGE)
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "match"

# --------------------------------------------------
# CSS FOR ACTIVE TOGGLE
# --------------------------------------------------
st.markdown("""
<style>
.toggle-btn > button {
    height: 3.2em;
    font-size: 1.05em;
    border-radius: 10px;
    border: 2px solid #d0d0d0;
    background-color: #f7f7f7;
}

.toggle-btn.active > button {
    background-color: #1f77b4 !important;
    color: white !important;
    border: 2px solid #1f77b4 !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Navigation Buttons (STABLE & PERSISTENT)
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    match_class = "toggle-btn active" if st.session_state.page == "match" else "toggle-btn"
    st.markdown(f'<div class="{match_class}">', unsafe_allow_html=True)
    st.button(
        "🏆 Predict Match Outcome",
        use_container_width=True,
        on_click=go_match,
        key="match_btn"
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    player_class = "toggle-btn active" if st.session_state.page == "player" else "toggle-btn"
    st.markdown(f'<div class="{player_class}">', unsafe_allow_html=True)
    st.button(
        "⭐ Predict Player Performance",
        use_container_width=True,
        on_click=go_player,
        key="player_btn"
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ==================================================
# MATCH OUTCOME PREDICTION
# ==================================================
if st.session_state.page == "match":

    st.header("🏆 Match Outcome Prediction")

    shots = st.number_input("Shots (Standardized)", value=2.5)
    passes = st.number_input("Total Passes", value=450)
    chances = st.number_input("Big Chances Created", value=3)
    yellow = st.number_input("Yellow Cards", value=2)
    red = st.number_input("Red Cards", value=0)

    if st.button("Predict Match Outcome"):

        raw_input = pd.DataFrame([{
            "Shots_std": shots,
            "Passes": passes,
            "Big chances created": chances,
            "Yellow cards": yellow,
            "Red cards": red
        }])

        aligned_input = strict_align_features(
            raw_input,
            clf_imputer.feature_names_in_
        )

        X = clf_imputer.transform(aligned_input)
        prediction = clf_model.predict(X)[0].lower()

        if prediction == "win":
            st.success("🟢🔥 **Strong chances of WINNING!** 🏆")
        elif prediction == "draw":
            st.info("⚖️🤝 **Looks like a DRAW — evenly matched.**")
        else:
            st.error("🔴😞 **High chances of LOSING the match.**")

# ==================================================
# PLAYER PERFORMANCE PREDICTION
# ==================================================
elif st.session_state.page == "player":

    st.header("⭐ Player Performance Prediction")

    assists = st.number_input("Assists", value=1.0)
    tackles = st.number_input("Tackles", value=20.0)
    clearances = st.number_input("Clearances", value=15.0)
    saves = st.number_input("Saves", value=0.0)
    clean_sheets = st.number_input("Clean Sheets", value=0.0)

    if st.button("Predict Player Performance"):

        raw_input = pd.DataFrame([{
            "Assists": assists,
            "Tackles": tackles,
            "Clearances": clearances,
            "Saves": saves,
            "Clean sheets": clean_sheets
        }])

        aligned_input = strict_align_features(
            raw_input,
            reg_imputer.feature_names_in_
        )

        X = reg_imputer.transform(aligned_input)
        raw_score = reg_model.predict(X)[0]

        relative_score = (raw_score / OBSERVED_MAX) * 5
        relative_score = max(0, min(relative_score, 5))

        stars = max(1, round(relative_score))

        labels = {
            1: "Poor 😞",
            2: "Below Average 😐",
            3: "Average 👍",
            4: "Strong 💪",
            5: "Elite 🌟"
        }

        st.subheader("🔍 Performance Evaluation")

        st.markdown(
            f"### {'⭐' * stars} ({stars}/5)\n"
            f"**{labels[stars]}**"
        )

        st.write(
            f"📈 **Predicted Performance Score:** `{raw_score:.2f}` "
            f"(relative rating: `{relative_score:.2f} / 5`)"
        )

        st.progress(relative_score / 5)








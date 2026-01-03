# ScoreSight — Predicting EPL Points Tally & Top Scorer

# Project Overview

ScoreSight is a machine learning project designed to predict English Premier League (EPL) match outcomes and player performance. By leveraging historical EPL data, the system forecasts match results, player goals, points tally, and top scorers. The project combines data preprocessing, feature engineering, model training, evaluation, and deployment in an interactive application, enabling real-time predictions.

# Objectives

Predict player performance (goals scored) using regression models.

Predict match outcomes (Win / Draw / Loss) using classification models.

Provide an interactive GUI for users to input match/player statistics and receive instant predictions.

Demonstrate end-to-end ML workflow from data handling to deployment.

# Features

Player Performance Prediction

Predict expected goals based on player statistics such as appearances, shots, passes, and assists.

Match Outcome Prediction

Predict whether a match will result in a Win, Draw, or Loss based on team performance statistics.

Interactive GUI

Built with Streamlit for a simple, user-friendly interface.

Model Integration

Random Forest Regression for goals prediction.

Gradient Boosting Classification for match outcome prediction.

# Tools & Technologies

Python – Data processing, ML models, scripting

Pandas / NumPy – Data manipulation

Scikit-learn – Model training and evaluation

Joblib – Model serialization


# Setup & Installation

# Clone the repository

git clone -b Tanisha-Bhowmik https://github.com/springboardmentor1979b-cmyk/ScoreSight---Predicting-EPL-Points-Tally-Top-Scorer.git
cd ScoreSight---Predicting-EPL-Points-Tally-Top-Scorer/Week-7


# Create a virtual environment

python -m venv venv


# Activate the virtual environment

venv\Scripts\activate


# Install dependencies

pip install -r requirements.txt


# Run the application

streamlit run app.py


# Usage

Open the Streamlit interface in your browser (usually http://localhost:8501).


# Navigate between tabs:

Player Performance – Input player stats to predict goals.

Match Outcome – Input match stats to predict Win/Draw/Loss.

Predictions are displayed instantly along with informative metrics.

# Screenshots

Player Performance Tab

Match Outcome Tab

Prediction Results


#  Conclusion

The ScoreSight project successfully integrates machine learning models with a user-friendly interface, enabling real-time prediction of EPL player and match outcomes. It demonstrates the full workflow of a data science project, from preprocessing to model deployment.



Streamlit – Web-based application interface

VS Code – Development environment

import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title("🌍 AQI Prediction App")
st.write("Enter pollution values to predict AQI")

# Store user inputs
input_data = []

for col in model_columns:
    value = st.number_input(f"Enter {col}", min_value=0.0, value=0.0)
    input_data.append(value)

# Predict button
if st.button("Predict AQI"):
    prediction = model.predict([input_data])[0]

    st.success(f"Predicted AQI: {round(prediction, 2)}")

    # AQI Category
    if prediction <= 50:
        st.info("Air Quality: Good 😊")
    elif prediction <= 100:
        st.info("Air Quality: Satisfactory 🙂")
    elif prediction <= 200:
        st.warning("Air Quality: Moderate 😐")
    elif prediction <= 300:
        st.warning("Air Quality: Poor 😷")
    else:
        st.error("Air Quality: Very Poor 🚨")

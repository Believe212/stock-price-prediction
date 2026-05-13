import streamlit as st
import pandas as pd
import joblib

# Load trained regression model
model = joblib.load("amzn_model.pkl")

st.title("Amazon Stock Price Predictor")

lag1 = st.number_input("AMZN Lag 1")
lag2 = st.number_input("AMZN Lag 2")
ma7 = st.number_input("AMZN MA7")

if st.button("Predict"):

    input_data = pd.DataFrame({
        "AMZN_lag1": [lag1],
        "AMZN_lag2": [lag2],
        "AMZN_MA7": [ma7]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Price: {prediction[0]:.2f}")
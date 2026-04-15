import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("🧬 BioPredict – Disease Risk Prediction")

features = []
for i in range(13):
    val = st.number_input(f"Feature {i+1}")
    features.append(val)

if st.button("Predict"):
    prediction = model.predict([features])
    st.write("Risk Level:", "High" if prediction[0] else "Low")

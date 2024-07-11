import streamlit as st
import numpy as np
import pandas as pd
import joblib


clf = joblib.load(open("titanic_model.pkl","rb"))

def predict(data):
    clf = joblib.load(open("titanic_model.pkls","rb"))
    return clf.predict(data)

st.title("Titanic Passenger Survival Prediction")
st.markdown("This model predicts whether a Titanic passenger survived or not based on input features.")


st.header("Traveler Details")


col1, col2 = st.columns(2)


with col1:
    age = st.slider("Age", 1, 100, 25)
    fare = st.slider("Ticket Fare", 0.0, 10000.0, 50.0)
    fs = st.slider("Family Size", 1, 10, 2)


with col2:
    pc = st.selectbox("Passenger Class", ["First Class", "Second Class", "Third Class"])
    bc = st.selectbox("Boarding From", ["Cherbourg", "Queenstown", "Southampton"])

# Convert passenger class and boarding location to numerical values
# For passenger class
if pc == "First Class":
    pc = 1
elif pc == "Second Class":
    pc = 2
else:
    pc = 3

# For boarding location
if bc == "Cherbourg":
    boarding = 1
elif bc == "Queenstown":
    boarding = 2
else:
    boarding = 3

# Prediction button
if st.button("Predict Survival"):
    result = clf.predict(np.array([[age,fare,fs,pc,boarding,1,1,1]]))
    st.text(result[0])
   

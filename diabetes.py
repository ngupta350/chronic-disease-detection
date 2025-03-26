import streamlit as st

def show():
    st.title("Diabetes Prediction")

    # User Input Fields
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, step=1)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, step=0.1)

    # Button to load results (does nothing for now)
    if st.button("Load Results"):
        st.write("Results will be displayed here in the future.")

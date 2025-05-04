import streamlit as st
import pandas as pd
import joblib
st.title("Car Price Prediction")
def load_model():
    model = joblib.load('LinearModel.pkl')  # or 'LinearModel.joblib' if saved with that extension
    return model

def toFrame(ls):
    column=['Name','Kms_driven','Fuel_type','Owner','Year','Company']
    frame=pd.DataFrame([ls],columns=column)
    return frame

def makePrediction(ls):
    model=load_model()
    data=toFrame(ls)
    result=model.predict(data)
    return result
    
    
with st.form("my_form"):
    st.write("Please fill out the form:")
    # Input fields
    name = st.text_input("Name")
    km_driven = st.number_input("Km_Driven", min_value=0)
    Fuel_Type = st.selectbox("Fuel_Type", ['Petrol', 'Diesel', 'Electric', 'Petrol + CNG', 'Hybrid', 'CNG'])
    Owner = st.selectbox("Owner", ['2nd Owner', '1st Owner', '3rd Owner'])
    year = st.number_input("Enter a year", min_value=1900, max_value=2100, step=1)
    company=st.text_input("Company Name")
    # Submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    ls=[name,km_driven,Fuel_Type,Owner,year,company]
    st.success(f"Price Predictions is {makePrediction(ls)[0]:.3f}")


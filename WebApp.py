#Importing the Requires Libraries & Model
import streamlit as st
import numpy as np
import pickle

### CSS Styling---------------------
st.markdown( 
    """
    <style>
    .st-emotion-cache-1629p8f.e1nzilvr2{
            text-align:center;      
    </style>
    """,
    unsafe_allow_html=True
)



### CSS Styling---------------------

def diabetes_prediction(input_data):
    model=pickle.load(open("saved_steps.sav","rb"))
    input_data_reshaped = np.array(input_data).reshape(1, -1)
    prediction=model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
        return "The Person is Non-Diabetic"
    else:
        return "The Person is Diabetic"
    
def main():
    st.title("Diabetes Prediction Web App")
    st.write("#### Diabetes prediction made easy, for a healthier you.")
    Pregnancies=st.text_input("No. of Preganencies",placeholder="0-17")
    Glucose=st.text_input("Glucose Level",placeholder="0-199")
    BloodPressure=st.text_input("BloodPressure Value",placeholder="0-122")
    SkinThickness=st.text_input("SkinThickness Value",placeholder="0-99")
    Insulin=st.text_input("Insulin Level",placeholder="0-846")
    BMI=st.text_input("BMI Value",placeholder="0.0-67.0")
    DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction Value",placeholder="0.078-2.420")
    Age=st.text_input("Age",placeholder="20-80")
    
    # Code For Prediction
    diagnosis=""
    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        st.success(diagnosis)
if __name__=="__main__":
    main()       
    
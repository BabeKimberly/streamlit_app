import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Preeclampsia prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load the saved model
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/trained_model.sav', 'rb'))

def preeclampsia_prediction(age, gest_age, diabp, sysbp, height, weight, bmi, fam_htn, htn, diabetes):
    # Simple prediction logic for demonstration
    if age and int(age) > 35 and sysbp and int(sysbp) > 140 and fam_htn == "Yes":
        return "The person is at high risk of preeclampsia."
    return "The person is not at high risk of preeclampsia."

def main():
    st.title('Preeclampsia Prediction Web Application')

    age = st.text_input('How old are you?')
    gest_age = st.text_input('How far along are you (Gestational age)')
    diabp = st.text_input('Systolic BP value (larger number)')
    sysbp = st.text_input('Diastolic BP value (smaller number)')
    height = st.text_input('Height (cm)')
    weight = st.text_input('Weight (kg)')
    bmi = st.text_input('BMI value')
    fam_htn = st.selectbox('Family history of Preeclampsia?', ['Yes', 'No'])
    htn = st.selectbox('Hypertension (high BP)?', ['Yes', 'No'])
    diabetes = st.selectbox('Diabetes (Sugar)?', ['Yes', 'No'])

    if st.button('Preeclampsia Test Result'):
        diagnosis = preeclampsia_prediction(age, gest_age, diabp, sysbp, height, weight, bmi, fam_htn, htn, diabetes)
        st.success(diagnosis)

if __name__ == '__main__':
    main()

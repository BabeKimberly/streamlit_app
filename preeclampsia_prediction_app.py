
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('C:/Users/LENOVO/Documents/dissertation research/Predictive Model/trained_model.sav', 'rb'))

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
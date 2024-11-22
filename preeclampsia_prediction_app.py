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
preeclampsia_model = pickle.load(open(f'{working_dir}/trained_model.sav', 'rb'))

#for  a sidebar navigatiom
with st.sidebar:
  selected = option_menu('Log in as', ['Specialist', 'Patient'], menu_icon = 'hospital-fill', icons = ['prediction', 'diagnosis'], default_index=0)

#to get specialist's input data
if selected == 'Specialist':
 
 
  #page title
  st.title == 'Specialist clinical results'
  
# Create 5 columns for input fields
col1, col2, col3, col4, col5 = st.columns(5)

# Add input fields in the first row of 5 columns
with col1:
    hb = st.text_input('Hemoglobin value')
with col2:
    pcv = st.text_input('PCV value')
with col3:
    tsh = st.text_input('Thyroid Stimulating Hormone')
with col4:
    platelet = st.text_input('Platelet count')
with col5:
    creatinine = st.text_input('Creatinine Levels')

# Add input fields in the second row of 5 columns
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    plgf_sflt = st.text_input('plgf_sflt value')
with col2:
    pp_13 = st.text_input('pp_13 value')
with col3:
    glycerides = st.text_input('Glycerides value')
with col4:
    seng = st.text_input('Soluble Endoglin (sEng) value')
with col5:
    cysc = st.text_input('Cystatin C (cysC)')

# Add input fields in the third row of 5 columns
col1, col2 = st.columns(2)  # Only 2 inputs for this row
with col1:
    diabetes = st.text_input('Is patient diabetic? (Yes/No)')
    diabetes = 1 if diabetes.lower() == 'yes' else 0  # Convert categorical to numerical
with col2:
 sp_art = st.text_input('Systolic Pulmonary Artery Pressure value')
     
    # code for Prediction
preeclampsia_diagnosis = ''

    # creating a button for Prediction
if st.button('Test Results'):
    try:
  # Collect user inputs
        user_input = [hb, pcv, tsh, platelet, creatinine, plgf_sflt, pp_13, glycerides,  seng,  cysc, diabetes, sp_art]

  # Convert inputs to floats (handle blank inputs gracefully)
        user_input = [float(x) for x in user_input]

        preeclampsia_prediction = preeclampsia_model.predict([user_input])

# Display results
if preeclampsia_prediction[0] == 1:
            preeclampsia_diagnosis = 'The person is diabetic'
else:
            preeclampsia_diagnosis = 'The person is not diabetic'

st.success(preeclampsia_diagnosis)

#error handling incase text is put in numerical data type
    except ValueError as e:
 st.error(f"Invalid input: {e}")

def preeclampsia_prediction(age, gest_age, diabp, sysbp, height, weight, bmi, fam_htn, htn, diabetes):
   
  # Simple prediction logic for demonstration
 if age and int(age) > 35 and sysbp and int(sysbp) > 140 and fam_htn == "Yes":
        return "The person is at high risk of Preeclampsia."
 return "The person is not at high risk of Preeclampsia."

 def main():
    st.title('Preeclampsia Prediction Web Application')

    age = st.text_input('How old are you?')
    gest_age = st.text_input('How far along are you (Gestational age)')
    diabp = st.text_input('Diastolic BP value (smaller BP reading)')
    sysbp = st.text_input('Systolic BP value (larger BP reading)')
    height = st.text_input('Height (cm)')
    weight = st.text_input('Weight (kg)')
    bmi = st.text_input('BMI value')
    fam_htn = st.selectbox('Family history of Preeclampsia?', ['Yes', 'No'])
    htn = st.selectbox('Hypertension (high BP)?', ['Yes', 'No'])

    # Convert categorical features to numerical
    htn = 1 if htn == 'Yes' else 0
    fam_htn = 1 if fam_htn == 'Yes' else 0

  # code for Prediction
    Preeclampsia_diagnosis = ''

    # creating a button for Prediction
    if st.button('My Preeclampsia Risk Test Results'):
      user_input = [age, gest_age, diabp, sysbp, height, weight, bmi, fam_htn, htn]

      user_input = [float(x) for x in user_input]

      Preeclampsia_prediction = heart_disease_model.predict([user_input])

      if Preeclampsia_prediction[0] == 1:
            Preeclampsia_diagnosis = 'The person is having Preeclampsia'
      else:
            Preeclampsia_diagnosis = 'The person is not at risk of Preeclampsia'
      st.success(Preeclampsia_diagnosis)


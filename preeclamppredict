import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/train_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Preeclampsia Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Preeclampsia Prediction Page
if selected == 'Preeclampsia Prediction':

    # page title
    st.title('Preeclampsia Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Enter your age')

    with col2:
        sysbp = st.text_input('Enter your diastolic pressure (the smaller BP reading)')

    with col3:
        diabp = st.text_input('Enter your systolic pressure (the larger BP reading)')

    with col1:
        weight = st.text_input('Enter your weight (kg)')

    with col2:
        height = st.text_input('Enter your height (cm)')

    with col3:
        BMI = st.text_input('BMI value')

    # code for Prediction
    preeclampsia_diagnosis = ''

    # creating a button for Prediction

    if st.button('Preeclampsia Test Result'):

        user_input = [age, sysbp, diabp, weight, height, BMI]
                      
        user_input = [float(x) for x in user_input]

        preeclampsia_prediction = preeclampsia_model.predict([user_input])

        if preeclampsia_prediction[0] == 1:
            preeclampsia_diagnosis = 'You are at high risk of having Preeclampsia'
        else:
            preeclampsia_diagnosis = 'You are not at risk of Preeclampsia'

    st.success(diab_diagnosis)

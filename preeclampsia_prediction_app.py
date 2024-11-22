import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Preeclampsia Prediction", layout="centered", page_icon="🧑‍⚕️")

# Load the saved model
working_dir = os.path.dirname(os.path.abspath(__file__))
preeclampsia_model = pickle.load(open(f'{working_dir}/trained_model.sav', 'rb'))

# Landing Page
def landing_page():
    st.title("Welcome to the Preeclampsia Prediction Web App")
    st.subheader("Choose your role and log in to continue")

    # Role selection
    role = st.selectbox("Log in as:", ["Select", "Specialist", "User"])

    # Input fields for credentials
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Log In"):
        # Validate inputs
        if role == "Select":
            st.error("Please select a role to proceed!")
        elif username == "" or password == "":
            st.error("Please enter both username and password!")
        else:
            if authenticate_user(role, username, password):
                st.success(f"Welcome, {username}! You have logged in as a {role}.")
                if role == "Specialist":
                    specialist_dashboard()
                elif role == "User":
                    user_dashboard()
            else:
                st.error("Invalid username or password. Please try again.")

# Authentication Function
def authenticate_user(role, username, password):
    # Add your personalized credentials here
    valid_credentials = {
        "Specialist": [ {"username": "specialist", "password": "specialist123"},  {"username": "KGC", "password": "KGC123"} ],
           
        "User": [{"username": "user", "password": "user123"}, {"username": "KGC", "password": "KGC123"}]
    }
    
    # Check if the role exists and validate the username/password
    if role in valid_credentials:
        for user in valid_credentials[role]:
            if user["username"] == username and user["password"] == password:
                return True
    return False

# Specialist Dashboard
def specialist_dashboard():
    st.title("Specialist Dashboard")

    # Patient Information Section
    st.header("Patient Information")
    patient_name = st.text_input("Patient's First Name", placeholder="Enter the patient's first name")
    patient_surname = st.text_input("Patient's Surname", placeholder="Enter the patient's surname")
    contact_number = st.text_input("Contact Number", placeholder="Enter the patient's contact number")
    id_number = st.text_input("National ID Number", placeholder="Enter the patient's ID number")
    hospital_number = st.text_input("Hospital Number (optional)", placeholder="Enter the hospital number (if available)")

    # Validate required fields for patient information
    if not patient_name or not patient_surname or not contact_number or not id_number:
        st.warning("All required fields (Name, Surname, Contact Number, ID Number) must be filled!")

    # Specialist Information Section
    st.header("Specialist Information")
    specialist_name = st.text_input("Specialist's Name", placeholder="Enter your name")
    specialist_workplace = st.text_input("Specialist's Workplace", placeholder="Enter hospital/clinic name")

    # Clinical Results Section
    st.header("Clinical Test Results")
    col1, col2, col3, col4, col5 = st.columns(5)

    # Add input fields in the first row of 5 columns
    with col1:
        hb = st.text_input('Hemoglobin value', placeholder="Enter hemoglobin value")
    with col2:
        pcv = st.text_input('PCV value', placeholder="Enter PCV value")
    with col3:
        tsh = st.text_input('Thyroid Stimulating Hormone', placeholder="Enter TSH value")
    with col4:
        platelet = st.text_input('Platelet count', placeholder="Enter platelet count")
    with col5:
        creatinine = st.text_input('Creatinine Levels', placeholder="Enter creatinine levels")

    # Second row of inputs
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        plgf_sflt = st.text_input('plgf_sflt value', placeholder="Enter plgf_sflt value")
    with col2:
        pp_13 = st.text_input('pp_13 value', placeholder="Enter pp_13 value")
    with col3:
        glycerides = st.text_input('Glycerides value', placeholder="Enter glycerides value")
    with col4:
        seng = st.text_input('Soluble Endoglin (sEng) value', placeholder="Enter sEng value")
    with col5:
        cysc = st.text_input('Cystatin C (cysC)', placeholder="Enter cystatin C value")

    # Third row of inputs
    col1, col2 = st.columns(2)
    with col1:
        diabetes = st.text_input('Is patient diabetic? (Yes/No)', placeholder="Enter Yes or No")
        diabetes = 1 if diabetes.lower() == 'yes' else 0  # Convert categorical to numerical
    with col2:
        sp_art = st.text_input('Systolic Pulmonary Artery Pressure value', placeholder="Enter systolic pressure value")

    # Initialize prediction variables
    preeclampsia_diagnosis = ''
    preeclampsia_prediction = None

    # Validate that required patient and specialist fields are filled
    if st.button('Test Results'):
        if not patient_name or not patient_surname or not contact_number or not id_number:
            st.error("Please fill in all required patient information fields!")
        elif not specialist_name or not specialist_workplace:
            st.error("Please fill in all required specialist information fields!")
        else:
            try:
                # Collect clinical test inputs
                user_input = [hb, pcv, tsh, platelet, creatinine, plgf_sflt, pp_13, 
                              glycerides, seng, cysc, diabetes, sp_art]

                # Convert inputs to floats (handle blank inputs gracefully)
                user_input = [float(x) if x != '' else 0.0 for x in user_input]

                # Make prediction
                preeclampsia_prediction = preeclampsia_model.predict([user_input])

            except ValueError as e:
                st.error(f"Invalid input: {e}")

    # Display results if prediction was successful
    if preeclampsia_prediction is not None:
        if preeclampsia_prediction[0] == 1:
            preeclampsia_diagnosis = 'The person is at risk of developing Preeclampsia'
        else:
            preeclampsia_diagnosis = 'The person is not at risk of developing Preeclampsia'
        
        # Display success message with patient and specialist details
        st.success(preeclampsia_diagnosis)
        st.write(f"**Patient Name**: {patient_name} {patient_surname}")
        st.write(f"**Contact Number**: {contact_number}")
        st.write(f"**ID Number**: {id_number}")
        if hospital_number:
            st.write(f"**Hospital Number**: {hospital_number}")
        st.write(f"**Specialist**: {specialist_name}")
        st.write(f"**Workplace**: {specialist_workplace}")

    # Display results if prediction was successful
    if preeclampsia_prediction is not None:
        if preeclampsia_prediction[0] == 1:
            preeclampsia_diagnosis = 'The person is at risk of developing Preeclampsia'
        else:
            preeclampsia_diagnosis = 'The person is not at risk of developing Preeclampsia'
        st.success(preeclampsia_diagnosis)

    st.write("Input clinical results and patient details below to predict preeclampsia risk.")


# User Dashboard
def user_dashboard():
    st.title("User Dashboard")

    age = st.text_input("Age")
    gest_age = st.text_input("Gestational Age")
    diabp = st.text_input("Diastolic Blood Pressure")
    sysbp = st.text_input("Systolic Blood Pressure")
    height = st.text_input("Height (cm)")
    weight = st.text_input("Weight (kg)")
    bmi = st.text_input("BMI")
    fam_htn = st.selectbox("Family history of hypertension?", ["Yes", "No"])
    htn = st.selectbox("History of hypertension?", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes?", ["Yes", "No"])

    # Convert categorical features to numerical
    fam_htn = 1 if fam_htn == 'Yes' else 0
    htn = 1 if htn == 'Yes' else 0
    diabetes = 1 if diabetes == 'Yes' else 0

    # Initialize prediction variables
    preeclampsia_diagnosis = ''
    preeclampsia_prediction = None

    # Create a button for Prediction
    if st.button('Calculate My Risk'):
        try:
            # Collect user inputs
            user_input = [age, gest_age, diabp, sysbp, height, weight, bmi, fam_htn, htn, diabetes]

            # Convert inputs to floats (handle blank inputs gracefully)
            user_input = [float(x) if x != '' else 0.0 for x in user_input]

            # Prediction
            preeclampsia_prediction = preeclampsia_model.predict([user_input])

        except ValueError as e:
            st.error(f"Invalid input: {e}")

    # Display results if prediction was successful
    if preeclampsia_prediction is not None:
        if preeclampsia_prediction[0] == 1:
            preeclampsia_diagnosis = 'You are at risk of developing Preeclampsia'
        else:
            preeclampsia_diagnosis = 'You are not at risk of developing Preeclampsia'
        st.success(preeclampsia_diagnosis)
        
    st.write("Enter personal details to check your risk of preeclampsia.")

# Run the app
landing_page()






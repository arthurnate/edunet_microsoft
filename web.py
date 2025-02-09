import os
import pickle
import streamlit as st
import streamlit_option_menu

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multi disease prdiction", layout="wide", page_icon="🦈")

diabetes_model = pickle.load(open(r"./training_models/diabetes_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"./training_models/parkinsons_model.sav", 'rb'))
heart_model = pickle.load(open(r"./training_models/heart_model.sav", 'rb'))


with st.sidebar:
    selected = option_menu("Disease Outbreak Prediction", ['Diabetes', 'Parkinsons', 'Heart'], menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

if selected == 'Diabetes':
    st.header("Predict Diabetes With Us")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        Bmi = st.text_input("BMI Value")
    with col1:
        DiabetesPedegreeFunction = st.text_input("Diabetes Pedegree Function Value")
    with col2:
        Age = st.text_input("Age")

    diabetes_diagnosis = ''

    if st.button('Predict Diabetes Results'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness , Insulin, Bmi, DiabetesPedegreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The person is DIABETIC'
        else:
            diabetes_diagnosis = 'The person is not DIABETIC'
    st.success(diabetes_diagnosis)


if selected == 'Parkinsons':
    st.header("Predict Parkinsons")
    col1, col2, col3 = st.columns(3)
    with col1:
        Fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        Flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        Jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        JitterAbs = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        Rap = st.text_input("MDVP:RAP")
    with col1:
        ppq = st.text_input("MDVP:PPQ")
    with col2:
        ddp = st.text_input("Jitter:DDP")
    with col3:
        shimmer = st.text_input("MDVP:Shimmer")
    with col1:
        shimmerDb = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        apq3 = st.text_input("Shimmer:APQ3")
    with col3:
        apq5 = st.text_input("Shimmer:APQ5")
    with col1:
        apq = st.text_input("MDVP:APQ")
    with col2:
        dda = st.text_input("Shimmer:DDA")
    with col3:
        nhr = st.text_input("NHR")
    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rdpe = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    with col1:
        s1 = st.text_input("spread1")
    with col2:
        s2 = st.text_input("spread2")
    with col3:
        d2 = st.text_input("D2")
    with col1:
        ppe = st.text_input("PPE")


    parkinson_diagnosis = ''

    if st.button('Predict Parkinsons Results'):
        user_input = [Fo, Fhi, Flo, Jitter , JitterAbs, Rap, ppq, ddp,shimmer, shimmerDb, apq3, apq5, apq, dda, nhr, hnr, rdpe, dfa, s1, s2, d2, ppe]
        user_input = [float(x) for x in user_input]
        parkinson_prediction = parkinsons_model.predict([user_input])

        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person has Parkinsons'
        else:
            parkinson_diagnosis = 'The person dose not have Parkinsons'
    st.success(parkinson_diagnosis)


if selected == 'Heart':
    st.header("Predict Hearh Health")
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input("Age")
    with col2:
        Sex = st.text_input("Sex")
    with col3:
        Cp = st.text_input("Cp")
    with col1:
        Thres = st.text_input("Threstbps")
    with col2:
        Chol = st.text_input("Cholestrol")
    with col3:
        Fbs = st.text_input("FBS")
    with col1:
        Rec = st.text_input("Restecg")
    with col2:
        Thalach = st.text_input("Thalach")
    with col3:
        Exang = st.text_input("Exang")
    with col1:
        op = st.text_input("Oldpeak")
    with col2:
        Slope = st.text_input("Slope")
    with col3:
        Ca = st.text_input("Ca")
    with col1:
        Thal = st.text_input("Thal")
    
    

    heart_diagnosis = ''

    if st.button('Predict Heart Disease Results'):
        user_input = [Age, Sex, Cp, Thres , Chol, Fbs, Rec, Thalach, Exang, op, Slope, Ca, Thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has Heart related issues'
        else:
            heart_diagnosis = 'The person dose NOT have Heart related issues'
    st.success(heart_diagnosis)

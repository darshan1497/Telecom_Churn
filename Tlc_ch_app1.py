# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""


@author: Darshan H M 
"""


import numpy as np # numpy used for mathematical operation on array
import pickle
import pandas as pd # pandas used for data manipulation on dataframe

import streamlit as st 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from PIL import Image


pickle_in = open("rf_clf.pkl","rb")
rf_clf=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
                                DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
                                SeniorCitizen,tenure,MonthlyCharges,TotalCharges):
    
    
   
    prediction=rf_clf.predict([[gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,
                                DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,
                                SeniorCitizen,tenure,MonthlyCharges,TotalCharges]])
    print(prediction)
    return prediction



def main():
    st.title("Telecom_Churn_Prediction")
    html_temp = """
    <body style="background-image: url("F:\Dockers-master\g1.jpg");
    background-size: cover;">
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">StreamlitTelecom_Churn_Prediction ML App </h2>
    </div>
    </body>
    """
   
    st.markdown(html_temp,unsafe_allow_html=True)

    
    gender= st.text_input("gender","Type Here")
    
   
   
    Partner=st.text_input("Partner","Type Here")
    
    Dependents = st.text_input("Dependents","Type Here")
    
    PhoneService = st.text_input("PhoneService","Type Here")

    display = ("Yes","No", "No phone service")
    options = list(range(len(display)))
    value = st.selectbox("MultipleLines", options, format_func=lambda x: display[x])
    MultipleLines=value
    
    display = ("Fiber optic","DSL", "No")
    options = list(range(len(display)))
    value = st.selectbox("InternetService", options, format_func=lambda x: display[x])
    InternetService=value
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("OnlineSecurity", options, format_func=lambda x: display[x])
    OnlineSecurity=value
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("OnlineBackup", options, format_func=lambda x: display[x])
    OnlineBackup=value
    
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("DeviceProtection", options, format_func=lambda x: display[x])
    DeviceProtection=value
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("TechSupport", options, format_func=lambda x: display[x])
    TechSupport=value
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("StreamingTV", options, format_func=lambda x: display[x])
    StreamingTV=value
    
    display = ("No","Yes", "No internet service")
    options = list(range(len(display)))
    value = st.selectbox("StreamingMovies", options, format_func=lambda x: display[x])
    StreamingMovies=value
    
    display = ("Month-to-month","Two year", "One year")
    options = list(range(len(display)))
    value = st.selectbox("Contract", options, format_func=lambda x: display[x])
    Contract=value
    
    display = ("Electronic check","Mailed check", "Bank transfer (automatic)", "Credit card (automatic)")
    options = list(range(len(display)))
    value = st.selectbox("PaymentMethod", options, format_func=lambda x: display[x])
    PaymentMethod=value
    

    
    
    
    PaperlessBilling = st.text_input("PaperlessBilling","Type Here")
    
    SeniorCitizen = st.text_input("SeniorCitizen","Type Here")
    tenure = st.text_input("tenure","Type Here")
    MonthlyCharges = st.text_input("MonthlyCharges","Type Here")
    TotalCharges = st.text_input("TotalCharges","Type Here")

   
    
    result=""
    if st.button("Predict"):
        
        gender=float(gender)
        Partner=float(Partner)
        Dependents=float(Dependents)
        PhoneService=float(PhoneService)
        MultipleLines=float(MultipleLines)
        InternetService=float(InternetService)
        OnlineSecurity=float(OnlineSecurity)
        OnlineBackup=float(OnlineBackup)
        DeviceProtection=float(DeviceProtection)
        TechSupport=float(TechSupport)
        StreamingTV=float(StreamingTV)
        StreamingMovies=float(StreamingMovies)
        Contract=float(Contract)
        PaperlessBilling=float(PaperlessBilling)
        PaymentMethod=float(PaymentMethod)
        SeniorCitizen=float(SeniorCitizen)
        tenure=float(tenure)
        MonthlyCharges=float(MonthlyCharges)
        TotalCharges=float(TotalCharges)
        
        
        
        
        result=predict_note_authentication(gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,SeniorCitizen,tenure,MonthlyCharges,TotalCharges)
    st.success('Telecom_Churn_Prediction is  {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
        option = st.selectbox('How would you like to be contacted?',({'Email':1, 'Home phone':2, 'Mobile phone':3}))
        st.write('You selected:', option)

if __name__=='__main__':
    main()
    
    
    
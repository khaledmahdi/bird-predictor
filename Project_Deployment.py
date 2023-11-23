import pandas as pd
import numpy as np
import streamlit as st
import pickle

#Upload Data

Data=pickle.load(open(r'C:\Users\user\Desktop\streamlit\Diabetes_prediction.sav','rb'))


st.title('Diabetes Prediction Web App')
st.info('Easy Application For Diabetes Prediction Deseas')
st.sidebar.header('Feature Selection')
st.write('khaled')
#st.line_chart(Data)
#'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 
#'DiabetesPedigreeFunction', 'Age'

Pregnancies=st.text_input('Pregnancies')
Glucose=st.text_input('Glucose')
BloodPressure=st.text_input('BloodPressure')
SkinThickness=st.text_input('SkinThickness')
Insulin=st.text_input('Insulin')
BMI=st.text_input('BMI')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
Age=st.text_input('Age')



df=pd.DataFrame({'Pregnancies':[Pregnancies],'Glucose':[Glucose],
              'BloodPressure':[BloodPressure],
              'SkinThickness':[SkinThickness],
              'Insulin':Insulin,'BMI':[BMI],
              'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],
              'Age':[Age]},index=[0])

Con=st.sidebar.button('Confirm')
if Con=="":
    st.write('Please Fill All The Fields')
else:
    if Con:
        result=Data.predict(df)
        if result==0:
            st.sidebar.write('The Patient Has not  Diabetes')
            st.sidebar.image('http://astrologer.swayamvaralaya.com/wp-content/uploads/2012/08/health1.jpg')
        else:
            st.sidebar.write('The Patient Has Diabetes')
            st.sidebar.image('https://asset-2.tstatic.net/palembang/foto/bank/images/diabetes5-diabetes4-diabetes3-diabetes2-diabetes1-diabetes.jpg')
        


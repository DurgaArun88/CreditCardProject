import streamlit as st
import pickle
import numpy as np
import gzip


dtc=pickle.load(gzip.open('dtc.pkl.gz','rb'))

st.title("CREDIT CARD FRAUD DETECTION")
st.write("This application predicts whether a transaction is valid or fraudulent based on the input data")

input_data = st.text_input('Enter the input data(comma separated values)','')


submit = st.button('Predict')

if submit:
   try:
      input_split_data = input_data.split(',')
      features = np.asarray(input_split_data, dtype=np.float32)
      prediction = dtc.predict(features.reshape(1,-1))

      if prediction[0]==0:
        st.success('Valid Transaction')
      else:
        st.error('Fraud Transaction')

   except ValueError:
    st.error('Invalid input')
   except Exception as e:
    st.error(f'An error occurred: {e}')

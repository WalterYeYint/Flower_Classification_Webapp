import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

#---------------------------------#
# Page layout
st.write("""
# Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")
st.sidebar.header('User Input Parameters')

#---------------------------------#

st.subheader('Class labels and their corresponding index number')
st.write("#Placeholder")

st.subheader('Prediction')
st.write("#Placeholder")
#st.write(prediction)

st.subheader('Prediction Probability')
st.write("#Placeholder")


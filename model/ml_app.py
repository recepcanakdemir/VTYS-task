import pickle
import numpy as np
import pandas as pd
import streamlit as st

df = pd.read_csv("../dataset/istanbul_satilik_evler_2023.csv")
with open('regression_model.pkl', 'rb') as file:
    reg = pickle.load(file)

def predict_price(Room, Area, Age, Floor):
    x = np.array([[Room, Area, Age, Floor]])
    return reg.predict(x)[0]

def run_ml_app():
    st.subheader('Please enter the required details:')
    Room = st.slider("Number of Rooms", 1, 10, step=1)
    Area = st.slider("Total Area in SqFt", 50, 1000, step=50)
    Age = st.slider("Age of the Property", 0, 100, step=1)
    Floor = st.slider("Floor Number", 0, 50, step=1)

    if st.button("Calculate Price"):
        result = predict_price(Room, Area, Age, Floor)
        st.success(f'Total Price: {result}')

if __name__ == '__main__':
    run_ml_app()

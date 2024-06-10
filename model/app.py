import streamlit as st
import streamlit.components.v1 as stc

from ml_app import run_ml_app
from eda_app import run_eda_app

html_temp = """
            <div style="background-color:#8A9A5B;padding:10px;border-radius:10px">
            <h1 style="color:white;text-align:center;"> Real Estate Price Prediction</h1>
            </div>
            """

def main():
    stc.html(html_temp)

    menu = ["Prediction", "EDA"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Prediction":
        run_ml_app()
    elif choice == "EDA":
        run_eda_app()

main()

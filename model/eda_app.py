import pandas as pd
from PIL import Image
import streamlit as st

def run_eda_app():
    st.subheader("Real Estate : Data Analysis")

    submenu = st.sidebar.selectbox("Submenu", ["Descriptive", "Plots"])
    df = pd.read_csv("istanbul_satilik_evler_2023.csv")

    if submenu == "Descriptive":
        st.dataframe(df)

        with st.expander("Data Types"):
            st.dataframe(df.dtypes)

        with st.expander("Data Summary"):
            st.dataframe(df.describe())

        with st.expander("Location Distribution"):
            st.dataframe(df["Location"].value_counts().head(30))

    elif submenu == "Plots":
        st.write("Plotting functionalities can be added here.")

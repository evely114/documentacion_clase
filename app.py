import streamlit as st
import pandas as pd

st.title("My Streamlit App")

df = pd.read_csv("data.csv")

st.write("Primera fila:", df.head())
st.write("Estadísticas:", df.describe())

columna = st.selectbox("Selecciona una columna", df.columns)

st.bar_chart(df[columna].value_counts())

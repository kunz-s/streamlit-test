import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly


st.title("Hello World")

st.write("*Data Science Course 2024*")

df = pd.read_csv("Bastar Craton.csv")

cat_names = df.columns.to_list()[27:]

col1, col2 = st.columns(2)

with col1:
    el1 = st.selectbox("yaxes", cat_names)
    st.write(el1)
with col2:
    el2 = st.selectbox("xaxes", cat_names)
    st.write(el2)
st.write(el1)

st.dataframe(df)

fig = plt.plot([1,2,3], [4,5,6])
st.pyplot(fig)
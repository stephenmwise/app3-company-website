import streamlit as st
import pandas

st.set_page_config("The Best Company | Home", layout="wide")

st.title("The Best Company")

subtext = """
The Best Company is a leading provider of innovative solutions tailored to meet the unique needs of our clients.
With a commitment to excellence, we deliver exceptional results and build lasting partnerships.
Our dedicated team of experts is passionate about driving success.
"""
st.write(subtext)
st.subheader("Our Team")

#Prepare columns
col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

#Get data from data.csv
df = pandas.read_csv("data.csv", sep=",")

# 3 column layout
with col1:
    #Iterate over first 4 rows
    for index, row in df[:4].iterrows():
        st.subheader(row["firstname"].capitalize() + " " + row["lastname"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("")
with col2:
    # Iterate over rows 4-8
    for index, row in df[4:8].iterrows():
        st.subheader(row["firstname"].capitalize() + " " + row["lastname"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("")
with col3:
    # Iterate over rows 8-12
    for index, row in df[8:].iterrows():
        st.subheader(row["firstname"].capitalize() + " " + row["lastname"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        st.write("")



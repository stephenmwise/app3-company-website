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
col1,col2,col3 = st.columns(3)

with col1:
    st.subheader("col1 text")
    st.write("Job Title")
    st.image("images/1.png")
with col2:
    st.subheader("col2 text")
    st.write("Job Title")
    st.image("images/2.png")
with col3:
    st.subheader("col3 text")
    st.write("Job Title")
    st.image("images/3.png")


import streamlit as st
import csv
import pandas

st.set_page_config("The Best Company | Contact Us", layout="wide")

st.title("Contact Us")
st.write("Have questions or need assistance? We're here to help! Please fill out the form below or contact us directly using the information provided. Our dedicated team is ready to assist you with your inquiries.")

#Form with text and subscribe checkbox
with st.form("my_form", clear_on_submit=True):
    st.write("Fill out this form with your inquiry to our team.")
    topics = pandas.read_csv("topics.csv")
    st.selectbox(label="Select Topic", options=topics["topic"])
    text_val = st.text_area("Write your message: ")
    checkbox_val = st.checkbox("Subscribe to newsletter (Updates, News, and Limited-time Deals)")
    # Submit Button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Thanks for your submission!", "We received your inquiry as ->", "MESSAGE:", "'", text_val, "'", ",", "SUBSCRIBED: ", checkbox_val)



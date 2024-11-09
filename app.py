import streamlit as st
st.title("GitHub-Workshop")
st.header("GIT, Belagavi")

name= st.text_input(label="Student Name", placeholder="Enter student name")
collageName= st.text_input(label="Collage", placeholder="Enter collage name")
email= st.text_input(label="Email", placeholder="Enter student email")


if st.button("Submit"):
    if name=="" or collageName=="" or email=="" :
        st.error("Please fill all the fields")
    else:
        st.success("Form submitted successfully")



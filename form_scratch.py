import streamlit as st
from datetime import datetime

min_date = datetime(1990, 1, 1)
max_date = datetime(2100, 1, 1)
st.title("User information form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
}

with st.form(key="user_info"): # this is important otherwise we rereun the app each time we change something
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter you height (cm): ")
    form_values["gender"] = st.checkbox("Gender", ["Male","Female"])
    form_values["dob"] = st.date_input("Enter your birthdate", 
                                       min_value=min_date, 
                                       max_value=max_date)



    submitt_button = st.form_submit_button("Submit")
    if submitt_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for key, value in form_values.items():
                st.write(f"{key}: {value}")
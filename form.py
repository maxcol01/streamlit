import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Form Demo")

# Form to hold the interactive elements
with st.form(key="simple_form"): # the data is collected only when pressing a button with this 
    # Text input
    st.subheader("Text Inputs")
    name = st.text_input("Enter you name")
    feedback = st.text_area("Provide your feedback")

    # Date and Time Inputs
    st.subheader("Date and Time inputs")
    dob = st.date_input("Selecy your data of birth")
    time = st.time_input("Choose a prefered time")

    # selectors
    st.subheader("Selectors")
    choice = st.radio("Choose an option", ["option 1", "option2"])
    gender = st.selectbox("Select you gender", ["Male","female"])
    slider_value = st.select_slider("Select a range", options=list(range(6)))

    # Toggles and checkboxes
    st.subheader("Toggles & Checkboxes")
    notifications = st.checkbox("Receive notifications ?")
    toggle_value = st.checkbox("Enable dark mode ?", value=False)
    button1 = st.form_submit_button("Submit")

    if button1:
        st.text(f"Hello {name}" )

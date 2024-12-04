import streamlit as st

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something",
                               value=st.session_state.user_input # grab the value from the state in order to preserve it
                               )
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", None)

st.write(f"User Input: {user_input}")
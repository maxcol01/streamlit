import streamlit as st

"""
Callabacks are function that can be called when performing something as it is below, we will encounter
somme issues ! (run the script for illustration) so to alleviate this -> callback
"""

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

if st.session_state.step == 1:
    st.header("Part 1: Info")

    name = st.text_input("Name", value=st.session_state.info.get("name",None))

    if st.button("Next"):
        st.session_state.info["name"] = name
        st.session_state.step = 2

if st.session_state.step == 2:
    st.header("Part 2: Review")

    st.subheader("Please review this: ")
    st.write(f"**Name**: {st.session_state.info.get('name', None)}")#key value pair

    if st.button("Submit"):
        st.success("Great")
        st.balloons()
        st.session_state.info = {}

    
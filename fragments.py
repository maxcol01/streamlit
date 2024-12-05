import streamlit as st

st.title("My awsome App !")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].toggle("Enter text")

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2].selectbox("Choose option: ", ["Option 1",
                                              "Option2",
                                              "Option3"
                                              ])
    new_cols[3].slider("Select value", min_value=0, max_value=100, value=50)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update"
               )
filter_and_file()
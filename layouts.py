import streamlit as st

# Sidebar layout
st.sidebar.title("This is a Sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter Something in the sidebar")

# Tabs layout
tab1, tab2, tab3 = st.tabs(["Tabs1","Tabs2", "Tabs3"])

with tab1:
    st.write("You are in tab1")
with tab2:
    st.write("You are in tab2")
with tab3:
    st.write("You are in tab3")

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.head("Column 2")
    st.write("Content for column 2")
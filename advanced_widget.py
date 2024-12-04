import streamlit as st

st.button("ok")
st.button("ok", key="btn2") # when creating elements that are identical -> manually identify by assigning a key (otherwise it is automatic and the key is the same since we passed the same parameters !)

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_val = st.slider("Set min value", min_value=0, max_value=50, value=25)
st.session_state.slider  = st.slider("Slider", min_val, 100, st.session_state.slider)
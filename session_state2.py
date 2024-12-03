import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter did not reset")
st.write(f"Counter value: {st.session_state.counter}")

"""
this is a way to store variables within a session (careful to not refresh)
this works like a key value pair. The initialization is done at the launch of the app 
"""
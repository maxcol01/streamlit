import streamlit as st

# A simple counter variable, without session state
counter = 0

st.write(f"Counter value: {counter}")

# Button to increment the counter
if st.button("Increment Counter: "):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")

    """
        the problem here is that because each time we press a button we rerun the app hence we never get
        passed the +1 since each time we reset the counter to O -> session state to alleviate this
    """
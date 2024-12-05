import streamlit as st

file_path = "example.txt"

@st.cache_resource
def get_file_handler():
    # Open the file in append mode which create the file if it does not exist
    file = open(file=file_path, mode="a+")
    return file

# Use the cached file handler
file_handler = get_file_handler()

# Write to the file using the cached handler
if st.button("Write to file"):
    file_handler.write("New line of text\n")
    file_handler.flush() # Ensure the content is written immdediately
    st.success("Wrote a new line to the file")

# Read and display the file contents
if st.button("Read File"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)
# Always make sure to close the file when done (useful ressource cleanup)
st.button("Close File", on_click=file_handler.close)
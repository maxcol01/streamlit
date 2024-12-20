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

# Container example
with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers as a grouping for elements.")
    st.write("Containers help manage section of the page.")

# Empty placeholder
placeholder = st.empty()
placeholder.write("this is a placeholder, useful for dynamic content.")

if st.button("Update place holder"):
    placeholder.write("The content of the placeholder has been updated")

#Expander
with st.expander("Expand for more details"):
    st.write("This is additional information that is hidden by default.")
    st.write("You can use expanders to keep your interface cleaner")

# Popover("Tooltip")
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover")

#Sidebar input handling
if sidebar_input:
    st.write(f"you entered in the sidebar: {sidebar_input}")
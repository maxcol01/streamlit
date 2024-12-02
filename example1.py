import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Streamlit Charts Demo")

# Generate sample data
char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

# Area Chart Selection
st.subheader("Area Chart")
st.area_chart(char_data)

# Bar Chart Section
st.subheader("Bar Chart")
st.bar_chart(char_data)

# Line Chart Section
st.subheader("Line Chart")
st.line_chart(char_data)

# Scatter Chart Section
st.subheader("Scatter Chart Section")
scatter_data = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})
st.scatter_chart(scatter_data)

# Map section (displaying random points on a map)
st.subheader("Map")
map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50,50] + [50.64, 5.57],
        columns=["lat","lon"]
)
st.map(map_data)

#Pyplot Section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(char_data["A"], label="A")
ax.plot(char_data["B"], label="B")
ax.plot(char_data["C"], label="C")
ax.set_title("Pyplot line chart")
ax.legend()
st.pyplot(fig)
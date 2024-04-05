import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

"""
# Welcome to my popular names app!

"""
names = pd.read_csv('popular_names.csv')
names['sex'] = names['sex'].astype(str)
genders = ['M', 'F']

name = "John"
gender = "M"

name = st.text_input("Enter name here")
gender = st.multiselect("Select gender", genders)
min_year = st.slider("Starting year", 1910, 2021, 1910)
max_year = st.slider("Ending year", 1910, 2021, 2021)

# Filter the data based on user input
filtered_data = names[names['name'] == name]
filtered_data = filtered_data[filtered_data['sex'] == gender]

# Create the line plot (with additional considerations for Streamlit)
fig, ax = plt.subplots()  # Create a figure and axis for better control
ax.plot(filtered_data['year'], filtered_data['n'])

# Customize the plot (optional)
ax.set_title('Count Over Time')  # Use ax.set_title for Streamlit compatibility
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.grid()

# Display the plot in Streamlit
st.pyplot(fig)

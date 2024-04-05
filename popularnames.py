_import altair as alt
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

user_name = "John"
user_gender = "M"

user_name = st.text_input("Enter name here")
user_gender = st.multiselect("Select gender", genders)
min_year = st.slider("Starting year", 1910, 2021, 1910)
max_year = st.slider("Ending year", 1910, 2021, 2021)

# Filter the data based on user input
filtered_data = names[names['name'] == user_name]
filtered_data = filtered_data[filtered_data['sex'] == user_gender]

# Create the line plot (with additional considerations for Streamlit)
fig, ax = plt.subplots()  # Create a figure and axis for better control
ax.plot(filtered_data['year'], filtered_data['n'])

# Customize the plot (optional)
ax.set_title('Popularity of ' + user_name + ' Over Time')  # Use ax.set_title for Streamlit compatibility
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.grid()

# Display the plot in Streamlit
st.pyplot(fig)

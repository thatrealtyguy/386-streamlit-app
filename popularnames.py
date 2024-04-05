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

# Create the density plot
fig, ax = plt.subplots()  # Create figure and axis for more control
filtered_data['year'].plot.density(ax=ax, color='red')  # Plot density on the prepared axis

# Customize the plot using Matplotlib functions
ax.set_title('Popularity of ' + name + ' Over Time')  # Set title with chosen name
ax.set_xlabel('Year')  # Set x-axis label
ax.set_xlim(1910, 2021)  # Set x-axis limits
ax.grid()  # Add gridlines

# Display the plot in Streamlit
st.pyplot(fig)

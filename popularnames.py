import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to my popular names app!

"""
data = pd.read_csv('popular_names.csv')
genders = ['M', 'F']

with st.tabs:
    name = st.text_input("Enter name here")

with st.sidebar:
    gender = st.multiselect("Select gender", genders)
    min_year = st.slider("Starting year", 1910, 2021, 1910)
    max_year = st.slider("Ending year", 1910, 2021, 2021)

# Filter the data based on user input
filtered_data = data[data['name'] == name]
filtered_data = data[data['sex'] == gender]

fig = px.histogram(filtered_data, x='year', title="Distribution of Chosen Name")
fig.update_layout(xaxis_range=[min_year, max_year])

# Display the plot using Streamlit's st.plotly_chart
st.plotly_chart(fig)

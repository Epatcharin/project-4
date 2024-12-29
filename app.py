import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt"

# Load the dataset
df = pd.read_csv(r"C:\Users\epatc\Downloads\vehicles_us (1).csv")

st.header("Car Advertisement Analysis Dashboard")


# Histogram for model years
st.subheader("Distribution of Model Years")
fig = px.histogram(df, x='model_year', color='model_year', 
                   title='Distribution of Model Years',
                   color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig)

# Scatter plot for model vs price
st.subheader("Model vs Price")
fig = px.scatter(df, x='model', y='price', 
                 title='Model vs Price',
                 color='model',
                 color_discrete_sequence=px.colors.qualitative.Vivid)
st.plotly_chart(fig)

# Checkbox to filter cars by odometer
if st.checkbox("Show cars with odometer below 100,000"):
    filtered_df = df[df['odometer'] < 100000]
    st.subheader("Price Distribution for Odometer < 100,000")
    fig = px.histogram(filtered_df, x='price', 
                       title='Price Distribution for Odometer < 100,000',
                       color='model',
                       color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig)

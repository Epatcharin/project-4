import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

st.write("""
# Vehical in U.S.
*CHART*
""")

# Load the dataset
df = pd.read_csv(r"C:\Users\epatc\Downloads\vehicles_us (1).csv"

st.line_chart(df)
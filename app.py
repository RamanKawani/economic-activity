import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data for cities and their economic activity (adjust this data to match your actual dataset)
data = {
    'City': ['Baghdad', 'Erbil', 'Basra', 'Mosul', 'Sulaymaniyah'],
    'GDP': [40, 15, 10, 5, 5],  # Example GDP values (adjust to your actual data)
    'Latitude': [33.3152, 36.1911, 30.0515, 36.3350, 35.5600],
    'Longitude': [44.3661, 44.0092, 47.8154, 43.1349, 45.4333],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create the map with Plotly
fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', hover_name='City', size='GDP',
                     projection="natural earth", title="Economic Activity in Iraq by City")

# Display the map in Streamlit
st.title("Economic Activity in Iraq")
st.plotly_chart(fig)

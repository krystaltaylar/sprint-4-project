import pandas as pd
import streamlit as st 
import altair as alt
import plotly.express as px 
from scipy import stats 

df = pd.read_csv("vehicles_us.csv")

# Add a header
st.header("Exploratory Data Analysis of Vehicles Dataset")

# Display a checkbox to show/hide a histogram
show_histogram = st.checkbox('Show Price Distribution Histogram')

if show_histogram:
    # Create a Plotly Express histogram for 'price'
    fig_hist =  px.histogram(df,
                      x='price',
                      labels={'price':'Price (USD)', 'condition':'Condition'},
                      color='condition',
                      title='Distribution of Prices')
    fig_hist.update_layout(yaxis_title='Amount')
    st.plotly_chart(fig_hist)  # Display the histogram in Streamlit

# Display a checkbox to show/hide a scatter plot
show_scatter = st.checkbox('Show Price vs Odometer Scatter Plot')

if show_scatter:
    # Create a Plotly Express scatter plot for 'price' vs 'odometer'
    fig_scatter = px.scatter(df,
                            x='model_year',
                            y='odometer',
                            color='fuel',
                            size='price',
                            labels={'model_year': 'Model Year',
                                    'odometer': 'Odometer Reading',
                                    'price': 'Price (USD)',
                                    'fuel': 'Fuel Type'},
                            title='Price vs Model Year and Odometer')
    st.plotly_chart(fig_scatter)  # Display the scatter plot in Streamlit

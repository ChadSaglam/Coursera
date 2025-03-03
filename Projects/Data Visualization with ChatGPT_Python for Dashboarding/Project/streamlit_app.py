import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
file_path = "Fenix-Shipping-Data.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Convert date column to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Sidebar filters
st.sidebar.header("Filter Data")
selected_country = st.sidebar.multiselect("Select Country", df['ship_country'].unique(), default=df['ship_country'].unique())
selected_shipper = st.sidebar.multiselect("Select Shipping Company", df['ship_via'].unique(), default=df['ship_via'].unique())
date_range = st.sidebar.date_input("Select Date Range", [df['order_date'].min(), df['order_date'].max()])

# Apply filters
df_filtered = df[df['ship_country'].isin(selected_country) & df['ship_via'].isin(selected_shipper)]
df_filtered = df_filtered[(df_filtered['order_date'] >= pd.Timestamp(date_range[0])) & (df_filtered['order_date'] <= pd.Timestamp(date_range[1]))]

# Line Chart: Freight Costs Over Time
fig_line = px.line(df_filtered, x='order_date', y='freight', title=f"Freight Costs Over Time")
st.plotly_chart(fig_line)

# Bar Chart: Total Freight Cost Per Month
df_filtered['month'] = df_filtered['order_date'].dt.to_period('M')
fig_bar = px.bar(df_filtered.groupby('month')['freight'].sum().reset_index(), x='month', y='freight', title="Total Freight Cost Per Month")
st.plotly_chart(fig_bar)

# Scatter Plot: Freight Cost vs Order Quantity
fig_scatter = px.scatter(df_filtered, x='quantity', y='freight', title="Freight Cost vs Order Quantity")
st.plotly_chart(fig_scatter)

# Pie Chart: Freight Cost Distribution by Shipping Company
fig_pie = px.pie(df_filtered, names='ship_via', values='freight', title="Freight Cost Distribution by Shipping Company")
st.plotly_chart(fig_pie)

# Histogram: Freight Cost Distribution
fig_hist = px.histogram(df_filtered, x='freight', title="Freight Cost Distribution")
st.plotly_chart(fig_hist)

# Data Preview
st.write("### Filtered Data Preview")
st.dataframe(df_filtered)

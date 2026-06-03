import streamlit as st
import pandas as pd

# Load CSV Data
df = pd.read_csv("system_logs.csv")

# Dashboard Title
st.title("Application Monitoring Dashboard")

# Show Data
st.subheader("System Logs")
st.dataframe(df)

# Calculate KPIs
avg_response = df["Response_Time"].mean()
total_errors = df["Errors"].sum()
avg_cpu = df["CPU_Usage"].mean()

# KPI Metrics
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Avg Response Time", f"{avg_response:.2f} ms")

with col2:
    st.metric("Total Errors", total_errors)

with col3:
    st.metric("Avg CPU Usage", f"{avg_cpu:.2f}%")

# Charts
st.subheader("CPU Usage Trend")
st.line_chart(df["CPU_Usage"])

st.subheader("Response Time Trend")
st.line_chart(df["Response_Time"])

st.subheader("Error Trend")
st.bar_chart(df["Errors"])

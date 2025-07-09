import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("realestate_data_southcarolina_2025.csv")

df = load_data()


st.title("📊 Data Science Dashboard")
st.markdown("A simple Streamlit app to explore and visualize datasets interactively.")

# Show dataset
if st.checkbox("Show raw data"):
    st.write(df)

# Column filter
columns = st.multiselect("Select columns to view", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[columns])

# Summary stats
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Categorical column selection
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

# Plot options
st.subheader("📊 Visualizations")

plot_type = st.selectbox("Choose plot type", ["Bar Chart", "Pie Chart", "Line Chart"])

if plot_type == "Bar Chart":
    x_col = st.selectbox("X-axis", categorical_cols)
    y_col = st.selectbox("Y-axis", numerical_cols)
    fig = px.bar(df, x=x_col, y=y_col, color=x_col)
    st.plotly_chart(fig)

elif plot_type == "Pie Chart":
    pie_col = st.selectbox("Pie Slice Category", categorical_cols)
    fig = px.pie(df, names=pie_col)
    st.plotly_chart(fig)

elif plot_type == "Line Chart":
    x_col = st.selectbox("X-axis", numerical_cols)
    y_col = st.selectbox("Y-axis", numerical_cols, index=1)
    fig = px.line(df, x=x_col, y=y_col)
    st.plotly_chart(fig)

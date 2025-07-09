import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Science Dashboard", layout="wide")
st.title("📊 Data Science Dashboard")

st.markdown("Upload your own CSV file or use the sample dataset.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload CSV", type=["csv"])

# Load CSV
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Use uploaded file or fallback to sample
if uploaded_file:
    df = load_data(uploaded_file)
    st.success("✅ Uploaded file loaded successfully.")
else:
    df = load_data("sample_data.csv")
    st.info("ℹ️ No file uploaded. Using sample data.")

# Show DataFrame
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Select columns
columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[columns])

# Summary stats
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Chart section
st.subheader("📈 Create a Chart")
chart_type = st.selectbox("Choose a chart type", ["Bar Chart", "Pie Chart", "Line Chart"])

categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
numerical_cols = df.select_dtypes(include=["number"]).columns.tolist()

if chart_type == "Bar Chart":
    x = st.selectbox("X-axis (categorical)", categorical_cols)
    y = st.selectbox("Y-axis (numeric)", numerical_cols)
    fig = px.bar(df, x=x, y=y, color=x)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Pie Chart":
    pie_col = st.selectbox("Pie column (categorical)", categorical_cols)
    fig = px.pie(df, names=pie_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":
    x = st.selectbox("X-axis (numeric)", numerical_cols)
    y = st.selectbox("Y-axis (numeric)", numerical_cols, index=1)
    fig = px.line(df, x=x, y=y)
    st.plotly_chart(fig, use_container_width=True)

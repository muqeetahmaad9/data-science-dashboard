import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Science Dashboard", layout="wide")

st.title("📊 Data Science Dashboard")
st.markdown("Upload your own CSV file or use the sample dataset to explore and visualize your data interactively.")

# 1. File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# 2. Load Data
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# 3. Determine data source
if uploaded_file:
    df = load_data(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    df = load_data("sample_data.csv")
    st.info("ℹ️ Using sample dataset (tips.csv)")

# 4. Show raw data
if st.checkbox("🔍 Show Raw Data"):
    st.dataframe(df)

# 5. Select columns
columns = st.multiselect("📌 Select columns to display", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[columns])

# 6. Summary statistics
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# 7. Chart selection
st.subheader("📊 Create a Chart")

chart_type = st.selectbox("Choose chart type", ["Bar Chart", "Pie Chart", "Line Chart"])

categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

if chart_type == "Bar Chart":
    x_col = st.selectbox("X-axis (categorical)", categorical_cols)
    y_col = st.selectbox("Y-axis (numeric)", numerical_cols)
    fig = px.bar(df, x=x_col, y=y_col, color=x_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Pie Chart":
    pie_col = st.selectbox("Pie slices by (categorical)", categorical_cols)
    fig = px.pie(df, names=pie_col)
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":
    x_col = st.selectbox("X-axis (numeric)", numerical_cols)
    y_col = st.selectbox("Y-axis (numeric)", numerical_cols, index=1)
    fig = px.line(df, x=x_col, y=y_col)
    st.plotly_chart(fig, use_container_width=True)

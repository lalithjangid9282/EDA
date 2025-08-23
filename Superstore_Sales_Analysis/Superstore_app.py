import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a wide layout and a title for the Streamlit app
st.set_page_config(layout="wide", page_title="Superstore Sales Analysis")

@st.cache_data
def load_data():
    """
    Loads the Superstore dataset, performs necessary data type conversions,
    and handles caching for improved performance.
    """
    # Load data with 'latin-1' encoding to avoid UnicodeDecodeError
    df = pd.read_csv("Sperstore_Sales_Analysis/Sample Superstore.csv", encoding='latin-1')
    
    # Convert 'Order Date' column to datetime objects
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    
    # Extract month and year from the date
    df['Month'] = df['Order Date'].dt.month_name()
    df['Year'] = df['Order Date'].dt.year
    
    return df

# Load the data using the cached function
df = load_data()

# App title and introduction
st.title("Superstore Sales & Profit EDA Dashboard")
st.markdown("An interactive dashboard to explore sales and profit trends across different categories, regions, and segments.")

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["Sales & Profit Overview", "Trends", "Sub-Category Performance"])

with tab1:
    st.subheader("Sales and Profit by Category")
    category_group = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    category_group.plot(kind='bar', ax=ax)
    plt.title("Sales & Profit by Category")
    plt.ylabel("Amount ($)")
    st.pyplot(fig)

    st.subheader("Sales & Profit by Customer Segment")
    seg_perf = df.groupby('Segment')[['Sales', 'Profit']].sum()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    seg_perf.plot(kind='bar', ax=ax)
    plt.title("Sales & Profit by Customer Segment")
    plt.ylabel("Amount ($)")
    st.pyplot(fig)

with tab2:
    st.subheader("Profit by Region")
    region_profit = df.groupby('Region')['Profit'].sum().sort_values()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    region_profit.plot(kind='barh', color='skyblue', ax=ax)
    plt.title("Profit by Region")
    plt.xlabel("Profit ($)")
    st.pyplot(fig)
    
    st.subheader("Monthly Sales Trend")
    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    monthly_sales.index = monthly_sales.index.to_timestamp()
    
    fig, ax = plt.subplots(figsize=(12, 5))
    monthly_sales.plot(ax=ax)
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales ($)")
    st.pyplot(fig)

with tab3:
    st.subheader("Profit by Sub-Category")
    subcat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Profit')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    subcat['Profit'].plot(kind='barh', ax=ax, color=['red' if p < 0 else 'green' for p in subcat['Profit']])
    plt.title("Profit by Sub-Category")
    plt.xlabel("Profit ($)")
    st.pyplot(fig)

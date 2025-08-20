import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page configuration for wide layout and title
st.set_page_config(layout="wide", page_title="Flight Delay Analysis")

# Set Seaborn style
sns.set_style("darkgrid")

@st.cache_data
def load_data():
    """
    Loads the flight delay dataset, handles missing values, and performs data cleaning.
    """
    try:
        df = pd.read_csv("flights_sample_3m.zip", on_bad_lines='skip')
        
        # Correct column names and drop rows with missing values
        df.dropna(subset=['ARR_DELAY', 'DEP_DELAY'], inplace=True)
        
        # Convert FL_DATE to datetime and extract month
        df['FL_DATE'] = pd.to_datetime(df['FL_DATE'], errors='coerce')
        df['MONTH'] = df['FL_DATE'].dt.month
        
        # Create a route column
        df['ROUTE'] = df['ORIGIN'] + "-" + df['DEST']
        
        return df
    except FileNotFoundError:
        st.error("Error: 'flights_sample_3m.csv' not found.")
        st.info("Please download the file from Kaggle and place it in the same directory as this script.")
        return None

# Load the dataset
df = load_data()

# App title and introduction
st.title("Flight Delay Analysis Dashboard")
st.markdown("An interactive dashboard to explore key factors contributing to flight delays.")

if df is not None:
    # Sidebar for filters
    st.sidebar.header("Filters")
    selected_airline = st.sidebar.selectbox("Select an Airline", ["All"] + sorted(df['AIRLINE'].unique()))
    
    # Filter data based on sidebar selection
    filtered_df = df
    if selected_airline != "All":
        filtered_df = df[df['AIRLINE'] == selected_airline]

    # Display basic info
    st.write(f"Displaying data for: **{selected_airline}** airline.")
    st.write(f"Number of flights: {len(filtered_df)}")

    # Tabs for different analyses
    tab1, tab2, tab3 = st.tabs(["Overview", "Trends", "Delay Causes"])

    with tab1:
        st.header("Airline Performance & Most Delayed Routes")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Average Arrival Delay by Airline")
            airline_delays = filtered_df.groupby('AIRLINE')['ARR_DELAY'].mean().sort_values(ascending=False)
            fig1, ax1 = plt.subplots(figsize=(10, 5))
            sns.barplot(x=airline_delays.index, y=airline_delays.values, hue=airline_delays.index, legend=False, ax=ax1)
            plt.ylabel("Avg Delay (minutes)")
            plt.xlabel("Airline")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig1)

        with col2:
            st.subheader("Top 10 Most Delayed Routes")
            route_delays = filtered_df.groupby('ROUTE')['ARR_DELAY'].mean().sort_values(ascending=False).head(10)
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.barplot(x=route_delays.values, y=route_delays.index, hue=route_delays.index, legend=False, ax=ax2)
            plt.xlabel("Avg Arrival Delay (minutes)")
            plt.tight_layout()
            st.pyplot(fig2)
            
    with tab2:
        st.header("Monthly Delay Trends")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Average Arrival Delay by Month")
            monthly_avg_delay = filtered_df.groupby('MONTH')['ARR_DELAY'].mean()
            fig3, ax3 = plt.subplots(figsize=(10, 5))
            ax3.plot(monthly_avg_delay, marker='o')
            plt.title("Average Arrival Delay by Month")
            plt.xlabel("Month")
            plt.ylabel("Avg Arrival Delay (minutes)")
            plt.grid(True)
            plt.tight_layout()
            st.pyplot(fig3)
        
        with col2:
            st.subheader("Arrival Delay Distribution")
            fig4, ax4 = plt.subplots(figsize=(10, 5))
            sns.histplot(filtered_df['ARR_DELAY'], bins=100, kde=True, ax=ax4)
            plt.title("Arrival Delay Distribution")
            plt.xlabel("Arrival Delay (minutes)")
            plt.ylabel("Frequency")
            plt.xlim(-50, 300)
            plt.tight_layout()
            st.pyplot(fig4)
            
    with tab3:
        st.header("Analysis of Delay Causes")
        
        st.subheader("Total Delay by Cause")
        delay_cols = ['DELAY_DUE_CARRIER', 'DELAY_DUE_WEATHER', 'DELAY_DUE_NAS', 'DELAY_DUE_SECURITY', 'DELAY_DUE_LATE_AIRCRAFT']
        # Check if delay columns exist before trying to access them
        if all(col in filtered_df.columns for col in delay_cols):
            df_delay = filtered_df[delay_cols].dropna()
            df_delay_sum = df_delay.sum().sort_values(ascending=False)
            fig5, ax5 = plt.subplots(figsize=(8, 5))
            sns.barplot(x=df_delay_sum.index, y=df_delay_sum.values, hue=df_delay_sum.index, legend=False, ax=ax5)
            plt.title("Total Delay by Cause")
            plt.ylabel("Total Minutes")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig5)
        else:
            st.warning("Delay cause columns not found in the dataset.")

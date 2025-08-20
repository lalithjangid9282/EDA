import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Set Seaborn style
sns.set(style="darkgrid")

# Set a wide layout and a title for the Streamlit app
st.set_page_config(layout="wide", page_title="NYC Airbnb Data Analysis")

@st.cache_data
def load_data():
    """
    Loads the Airbnb dataset and performs necessary data cleaning.
    """
    try:
        df = pd.read_csv("AB_NYC_2019.csv")
    except FileNotFoundError:
        st.error("Error: 'AB_NYC_2019.csv' not found. Please upload the file or ensure it's in the same directory.")
        return None
    
    # Drop unnecessary columns
    df.drop(['id', 'name', 'host_name', 'last_review'], axis=1, inplace=True)
    
    # Fill missing values
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    
    return df

# Load the data using the cached function
df = load_data()

# App title and introduction
st.title("NYC Airbnb Data Analysis Dashboard")
st.markdown("An interactive dashboard to explore Airbnb listings in New York City.")

if df is not None:
    # Create tabs for better organization
    tab1, tab2, tab3, tab4 = st.tabs(["Price & Room Types", "Geospatial Map", "Availability", "Raw Data"])

    with tab1:
        st.header("Price and Room Type Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Price Distribution (Under $500)")
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.histplot(df[df['price'] < 500]['price'], bins=50, kde=True, ax=ax)
            plt.xlabel("Price")
            plt.title("Price Distribution")
            st.pyplot(fig)

        with col2:
            st.subheader("Room Type Distribution")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.countplot(x='room_type', data=df, ax=ax2)
            plt.title("Room Type Distribution")
            st.pyplot(fig2)

        st.subheader("Average Price by Borough")
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        sns.barplot(x='neighbourhood_group', y='price', data=df[df['price'] < 500], ax=ax3)
        plt.title("Average Price by Borough")
        st.pyplot(fig3)

    with tab2:
        st.header("Geospatial Map of NYC Listings")
        
        # Folium map
        map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
        # Sample 500 listings for performance
        sample_df = df[df['price'] < 500].sample(500)
        for _, row in sample_df.iterrows():
            folium.CircleMarker(
                [row["latitude"], row["longitude"]],
                radius=1,
                color='blue',
                fill=True,
                fill_opacity=0.5
            ).add_to(map_nyc)
        
        # Display the map in the Streamlit app
        folium_static(map_nyc)
        st.info("The map displays a sample of 500 listings with prices under $500.")

    with tab3:
        st.header("Availability Analysis")
        st.subheader("Availability Over the Year")
        fig4, ax4 = plt.subplots(figsize=(10, 5))
        sns.histplot(df['availability_365'], bins=30, kde=True, ax=ax4)
        plt.title("Availability Over the Year")
        plt.xlabel("Days Available")
        st.pyplot(fig4)

    with tab4:
        st.header("Raw Data Overview")
        st.dataframe(df.head(20))

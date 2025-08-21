import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a wide layout and a title for the Streamlit app
st.set_page_config(layout="wide", page_title="Spotify Data Analysis")

# Set Seaborn style
sns.set(style="darkgrid")

@st.cache_data
def load_data():
    """
    Loads the Spotify dataset and performs necessary data cleaning.
    """
    try:
        df = pd.read_csv("Spotify.csv")
    except FileNotFoundError:
        st.error("Error: 'Spotify.csv' not found. Please ensure the file is in the same directory.")
        return None
    
    # Drop duplicates or nulls if any
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    
    return df

# Load the data using the cached function
df = load_data()

# App title and introduction
st.title("Spotify Data Analysis Dashboard")
st.markdown("An interactive dashboard to explore music features and popularity.")

if df is not None:
    # Sidebar for filters
    st.sidebar.header("Filters")
    selected_genre = st.sidebar.selectbox("Select a Genre", ["All"] + sorted(df['genre'].unique()))
    
    # Filter data based on sidebar selection
    filtered_df = df
    if selected_genre != "All":
        filtered_df = df[df['genre'] == selected_genre]

    # Display basic info
    st.write(f"Displaying data for: **{selected_genre}** genre.")
    st.write(f"Number of songs: {len(filtered_df)}")
    
    # Tabs for navigation
    tab1, tab2 = st.tabs(["Overview & Correlation", "Feature Distribution"])

    with tab1:
        st.header("Overview and Correlation Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Correlation Matrix")
            # Calculate correlation for the filtered data
            corr = filtered_df[['popularity', 'tempo', 'energy', 'valence', 'loudness', 'danceability']].corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Top 10 Genres by Average Popularity")
            # This plot uses the full dataset to show top genres overall
            genre_pop = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
            fig2, ax2 = plt.subplots(figsize=(12, 6))
            sns.barplot(x=genre_pop.index, y=genre_pop.values, hue=genre_pop.index, palette="viridis", legend=False, ax=ax2)
            plt.xticks(rotation=45)
            plt.ylabel("Average Popularity")
            st.pyplot(fig2)

    with tab2:
        st.header("Feature Distribution Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Tempo Distribution")
            fig3, ax3 = plt.subplots(figsize=(10, 5))
            sns.histplot(filtered_df['tempo'], bins=50, kde=True, color='purple', ax=ax3)
            plt.xlabel("Tempo")
            st.pyplot(fig3)

        with col2:
            st.subheader("Energy Distribution")
            fig4, ax4 = plt.subplots(figsize=(10, 5))
            sns.histplot(filtered_df['energy'], bins=50, kde=True, color='orange', ax=ax4)
            plt.xlabel("Energy")
            st.pyplot(fig4)

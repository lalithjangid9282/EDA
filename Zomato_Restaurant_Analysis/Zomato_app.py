import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Zomato Restaurant Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv("zomato.csv", encoding='latin-1', dtype={"column_name": str})

    df = df[df['rate'].notnull() & (df['rate'] != 'NEW') & (df['rate'] != '-')]
    df['rate'] = df['rate'].apply(lambda x: str(x).split('/')[0]).str.strip()
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
    df = df[df['rate'].notnull()]
    df['cuisines'] = df['cuisines'].astype(str)
    return df

df = load_data()

st.title("Zomato Restaurant EDA")
st.markdown("Explore restaurant distribution, ratings, cuisines, and pricing trends.")

tab1, tab2, tab3 = st.tabs([" City-wise Restaurants", "⭐ Ratings", "Cuisines & Pricing"])

with tab1:
    st.subheader("Top 10 Locations by Restaurant Count")
    city_count = df['location'].value_counts().head(10)
    fig, ax = plt.subplots()
    city_count.plot(kind='bar', color='orange', ax=ax)
    ax.set_ylabel("Number of Restaurants")
    st.pyplot(fig)

with tab2:
    st.subheader("Rating Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['rate'], bins=20, kde=True, ax=ax, color='green')
    ax.set_xlabel("Rating")
    st.pyplot(fig)

with tab3:
    st.subheader("Top Cuisines")
    cuisine_series = df['cuisines'].str.split(', ').explode()
    top_cuisines = cuisine_series.value_counts().head(10)
    fig, ax = plt.subplots()
    top_cuisines.plot(kind='barh', color='lightblue', ax=ax)
    ax.invert_yaxis()
    ax.set_xlabel("Count")
    st.pyplot(fig)

    st.subheader("Price Range vs Rating")
    if 'price_range' in df.columns:
        fig, ax = plt.subplots()
        sns.boxplot(x='price_range', y='rate', data=df, ax=ax, palette='pastel')
        ax.set_xlabel("Price Range (1 = Low, 4 = High)")
        st.pyplot(fig)
    else:
        st.warning("Price range data not available in this dataset.")

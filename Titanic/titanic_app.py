import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a wide layout and a title for the Streamlit app
st.set_page_config(layout="wide", page_title="Titanic Survival Analysis")

@st.cache_data
def load_data():
    """
    Loads and cleans the Titanic dataset.
    Caches the data to improve performance on subsequent runs.
    """
    # Load the dataset
    df = pd.read_csv("Titanic/titanic.csv")
    
    # Handle missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    if 'Cabin' in df.columns:
        df.drop(columns='Cabin', inplace=True)
    if 'Embarked' in df.columns:
        df.dropna(subset=['Embarked'], inplace=True)
    
    return df

# Load the cleaned data
df = load_data()

# App title and introduction
st.title("Titanic Survival EDA Dashboard")
st.markdown("An interactive dashboard to explore survival patterns on the Titanic.")

# Sidebar for filtering
st.sidebar.header("Filter")
selected_pclass = st.sidebar.selectbox("Select Passenger Class", options=["All", 1, 2, 3])
selected_gender = st.sidebar.selectbox("Select Gender", options=["All", "male", "female"])

filtered_df = df.copy()

if selected_pclass != "All":
    filtered_df = filtered_df[filtered_df['Pclass'] == selected_pclass]
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df['Sex'] == selected_gender]

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["Survival Overview", "Gender & Class", "Age Analysis"])

with tab1:
    st.subheader("Overall Survival Distribution")
    
    # Pie Chart
    survived_counts = filtered_df['Survived'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(
        survived_counts, 
        autopct='%1.1f%%', 
        labels=['Not Survived', 'Survived'],
        colors=['lightcoral', 'lightgreen'],
        startangle=90
    )
    ax1.set_title('Survival Distribution')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    st.subheader("Survival Count")
    fig2, ax2 = plt.subplots()
    sns.countplot(x='Survived', data=filtered_df, palette='Set2', hue='Survived', legend=False, ax=ax2)
    ax2.set_xticklabels(['Not Survived', 'Survived'])
    ax2.set_title("Survival Count")
    st.pyplot(fig2)

with tab2:
    st.subheader("Survival by Gender")
    fig3, ax3 = plt.subplots()
    sns.countplot(x='Sex', hue='Survived', data=filtered_df, palette='pastel', ax=ax3)
    ax3.set_title("Survival by Gender")
    ax3.legend(labels=['Not Survived', 'Survived'])
    st.pyplot(fig3)

    st.subheader("Survival by Passenger Class")
    fig4, ax4 = plt.subplots()
    sns.countplot(x='Pclass', hue='Survived', data=filtered_df, palette='coolwarm', ax=ax4)
    ax4.set_title("Survival by Passenger Class")
    ax4.legend(labels=['Not Survived', 'Survived'])
    st.pyplot(fig4)

with tab3:
    st.subheader("Age vs Survival")
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.histplot(data=filtered_df, x='Age', hue='Survived', multiple='stack', palette='Accent', bins=30, ax=ax5)
    ax5.set_title("Age vs Survival")
    st.pyplot(fig5)

    st.subheader("Age Distribution by Survival")
    fig6, ax6 = plt.subplots()
    sns.boxplot(x='Survived', y='Age', data=filtered_df, palette='spring', hue='Survived', legend=False, ax=ax6)
    ax6.set_xticklabels(['Not Survived', 'Survived'])
    ax6.set_title("Age Distribution by Survival")
    st.pyplot(fig6)

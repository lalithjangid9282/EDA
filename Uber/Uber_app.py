import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import calendar

st.set_page_config(layout="wide")

st.title(" Uber NYC Trip Explorer")
df = pd.read_csv('Uber/Uber_Data.csv')
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour
df['DayOfWeek'] = df['Date/Time'].dt.dayofweek
df['Day'] = df['Date/Time'].dt.day
df['Weekday'] = df['DayOfWeek'].apply(lambda x: calendar.day_name[x])

# Sidebar Filters
st.sidebar.header(" Filter Options")
selected_day = st.sidebar.selectbox("Select Day", sorted(df['Day'].unique()))
selected_hour = st.sidebar.slider("Select Hour", 0, 23, 12)

filtered_df = df[(df['Day'] == selected_day) & (df['Hour'] == selected_hour)]

# Display Map
st.subheader(f" Pickup Map for Day {selected_day}, Hour {selected_hour}")
pickup_map = folium.Map(location=[40.75, -73.95], zoom_start=12)
heat_data = filtered_df[['Lat', 'Lon']].dropna().values.tolist()
HeatMap(heat_data[:10000]).add_to(pickup_map)
folium_static(pickup_map)

# Plots
st.subheader(" Trips by Hour of Day")
fig, ax = plt.subplots()
sns.countplot(x='Hour', data=df, ax=ax)
st.pyplot(fig)

st.subheader(" Trips by Weekday")
fig2, ax2 = plt.subplots()
sns.countplot(x='Weekday', data=df, order=calendar.day_name, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

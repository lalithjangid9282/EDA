import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Load data
print("Loading dataset 'AB_NYC_2019.csv'...")
df = pd.read_csv("../AB_NYC_2019.csv")
print("Dataset loaded successfully. Displaying first 5 rows:")
print(df.head())

# Basic stats
print("\nDisplaying basic dataset information and statistics...")
print(df.info())
print(df.describe())
print("Information and statistics displayed.")

# Drop unnecessary columns
print("\nDropping unnecessary columns: 'id', 'name', 'host_name', 'last_review'...")
df.drop(['id', 'name', 'host_name', 'last_review'], axis=1, inplace=True)
print("Columns dropped successfully.")

# Fill missing values
print("\nFilling missing values in 'reviews_per_month' with 0...")
df['reviews_per_month']=df['reviews_per_month'].fillna(0)
print("Missing values filled.")

# Price distribution
print("\nGenerating Price Distribution (Under $500) chart...")
plt.figure(figsize=(10, 5))
sns.histplot(df[df['price'] < 500]['price'], bins=50, kde=True)
plt.title("Price Distribution (Under $500)")
plt.xlabel("Price")
plt.show()
print("Chart displayed: Price Distribution.")

# Room type counts
print("\nGenerating Room Type Distribution chart...")
plt.figure(figsize=(6, 4))
sns.countplot(x='room_type', data=df)
plt.title("Room Type Distribution")
plt.show()
print("Chart displayed: Room Type Distribution.")

# Listings per Borough
print("\nGenerating Listings by Borough chart...")
plt.figure(figsize=(8, 5))
sns.countplot(x='neighbourhood_group', data=df, order=df['neighbourhood_group'].value_counts().index)
plt.title("Listings by Borough")
plt.show()
print("Chart displayed: Listings by Borough.")

# Average price per borough
print("\nGenerating Average Price by Borough chart...")
plt.figure(figsize=(8, 5))
sns.barplot(x='neighbourhood_group', y='price', data=df[df['price'] < 500])
plt.title("Average Price by Borough")
plt.show()
print("Chart displayed: Average Price by Borough.")

# Availability
print("\nGenerating Availability Over the Year chart...")
plt.figure(figsize=(10, 5))
sns.histplot(df['availability_365'], bins=30, kde=True)
plt.title("Availability Over the Year")
plt.xlabel("Days Available")
plt.show()
print("Chart displayed: Availability Over the Year.")

# Folium heatmap
print("\nGenerating Folium heatmap of NYC Airbnb listings...")
map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
for idx, row in df[df['price'] < 500].sample(500).iterrows():
    folium.CircleMarker(
        [row["latitude"], row["longitude"]],
        radius=1,
        color='blue',
        fill=True,
        fill_opacity=0.5
    ).add_to(map_nyc)
map_nyc.save("NYC_Airbnb_Map.html")
print("Folium map saved as 'NYC_Airbnb_Map.html'.")

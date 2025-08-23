import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import calendar

# Load Dataset
print("Loading dataset...")
df = pd.read_csv('../Uber_Data.csv')
print("Dataset loaded successfully.")

# Convert 'Date/Time' column to datetime objects with the correct format
print("\nConverting 'Date/Time' column...")
df['Date/Time'] = pd.to_datetime(df['Date/Time'], format='%m/%d/%Y %H:%M:%S')
print("Date/Time conversion complete.")

# Feature Engineering
print("Extracting time-based features...")
df['Hour'] = df['Date/Time'].dt.hour
df['DayOfWeek'] = df['Date/Time'].dt.dayofweek
df['Day'] = df['Date/Time'].dt.day
df['Month'] = df['Date/Time'].dt.month
df['Weekday'] = df['DayOfWeek'].apply(lambda x: calendar.day_name[x])
print("Features extracted successfully.")

# === Plotting and Analysis ===

# Plot hourly trip frequency
print("\nGenerating Trips by Hour of Day chart...")
plt.figure(figsize=(10,5))
sns.countplot(x='Hour', data=df)
plt.title('Trips by Hour of Day')
plt.show()
print("Displayed: Trips by Hour of Day")

# Plot weekday patterns
print("\nGenerating Trips by Day of Week chart...")
plt.figure(figsize=(10,5))
sns.countplot(x='Weekday', data=df, order=calendar.day_name)
plt.title('Trips by Day of Week')
plt.xticks(rotation=45)
plt.show()
print("Displayed: Trips by Day of Week")

# Heatmap: Hour vs Day of Week
print("\nGenerating Heatmap: Hour vs Day of Week...")
heatmap_data = df.groupby(['Hour', 'DayOfWeek']).size().unstack()
plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, cmap='YlGnBu')
plt.title('Heatmap: Hour vs Day of Week')
plt.show()
print("Displayed: Heatmap: Hour vs Day of Week")

# Folium Map of Pickup Locations
print("\nGenerating Folium Map of Pickup Locations...")
pickup_map = folium.Map(location=[40.75, -73.95], zoom_start=12)
heat_data = df[['Lat', 'Lon']].dropna().values.tolist()
HeatMap(heat_data[:10000]).add_to(pickup_map)
# Display the map. It will not be saved as a file.
print("Map prepared for display.")
pickup_map.save('nyc_pickup_map.html')

# === Done ===
print("\nEDA Completed.")



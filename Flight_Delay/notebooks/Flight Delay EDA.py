import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
# The original Kaggle link is a webpage, not a raw file.
# Please download the 'flights_sample_3m.csv' file from Kaggle and place it in the same directory.
print("Loading dataset from local file 'flights_sample_3m.csv'...")
try:
    # Fix: Added on_bad_lines='skip' to handle potential malformed rows in the CSV
    df = pd.read_csv("../flights_sample_3m.csv", on_bad_lines='skip')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'flights_sample_3m.csv' not found.")
    print("Please download the file from Kaggle and place it in the same directory as this script.")
    exit()

print(f"\nDataset shape: {df.shape}")
print(f"Dataset columns: {df.columns.tolist()}")

# Basic info
print("\nChecking for missing values in key columns...")
# Fix: Corrected column names from 'ARRIVAL_DELAY'/'DEPARTURE_DELAY' to 'ARR_DELAY'/'DEP_DELAY'
if 'ARR_DELAY' in df.columns and 'DEP_DELAY' in df.columns:
    print(df[['ARR_DELAY', 'DEP_DELAY']].isnull().sum())
    df = df.dropna(subset=['ARR_DELAY', 'DEP_DELAY'])
    print("Rows with missing ARR_DELAY or DEP_DELAY values have been removed.")
    print(f"New dataset shape: {df.shape}")
else:
    print("Error: 'ARR_DELAY' or 'DEP_DELAY' column not found.")
    # Exit or handle the missing columns appropriately
    exit()

# Convert dates if needed
# Fix: 'MONTH' column is not available, extracting month from 'FL_DATE'
print("\nConverting date column and extracting month...")
if 'FL_DATE' in df.columns:
    df['FL_DATE'] = pd.to_datetime(df['FL_DATE'], errors='coerce')
    df['MONTH'] = df['FL_DATE'].dt.month
else:
    print("Error: 'FL_DATE' column not found. Cannot extract month.")
    exit()
# The 'DAY_OF_WEEK' column is not available and has been removed.

# Airline delay averages
print("\nGenerating Average Arrival Delay by Airline chart...")
# Fix: Corrected column name to 'ARR_DELAY'
airline_delays = df.groupby('AIRLINE')['ARR_DELAY'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=airline_delays.index, y=airline_delays.values, hue=airline_delays.index, legend=False)
plt.title("Average Arrival Delay by Airline")
plt.ylabel("Avg Delay (minutes)")
plt.xlabel("Airline")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Chart displayed: Average Arrival Delay by Airline.")

# Delay reason analysis
print("\nGenerating Total Delay by Cause chart...")
# Fix: Corrected column names to match the dataset
delay_cols = ['DELAY_DUE_CARRIER', 'DELAY_DUE_WEATHER', 'DELAY_DUE_NAS', 'DELAY_DUE_SECURITY', 'DELAY_DUE_LATE_AIRCRAFT']
df_delay = df[delay_cols].dropna()
df_delay_sum = df_delay.sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
# Renamed x-tick labels for clarity
sns.barplot(x=df_delay_sum.index, y=df_delay_sum.values, hue=df_delay_sum.index, legend=False)
plt.title("Total Delay by Cause")
plt.ylabel("Total Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Chart displayed: Total Delay by Cause.")

# Monthly delay trend
print("\nGenerating Average Arrival Delay by Month chart...")
# Fix: Corrected column name to 'ARR_DELAY'
monthly_avg_delay = df.groupby('MONTH')['ARR_DELAY'].mean()
plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_delay, marker='o')
plt.title("Average Arrival Delay by Month")
plt.xlabel("Month")
plt.ylabel("Avg Arrival Delay")
plt.grid(True)
plt.tight_layout()
plt.show()
print("Chart displayed: Average Arrival Delay by Month.")

# Most delayed routes
print("\nGenerating Top 10 Most Delayed Routes chart...")
# Fix: Corrected column names to 'ORIGIN' and 'DEST'
df['ROUTE'] = df['ORIGIN'] + "-" + df['DEST']
# Fix: Corrected column name to 'ARR_DELAY'
route_delays = df.groupby('ROUTE')['ARR_DELAY'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=route_delays.values, y=route_delays.index, hue=route_delays.index, legend=False)
plt.title("Top 10 Most Delayed Routes")
plt.xlabel("Avg Arrival Delay")
plt.tight_layout()
plt.show()
print("Chart displayed: Top 10 Most Delayed Routes.")

# Delay distribution
print("\nGenerating Arrival Delay Distribution histogram...")
plt.figure(figsize=(10, 5))
# Fix: Corrected column name to 'ARR_DELAY'
sns.histplot(df['ARR_DELAY'], bins=100, kde=True)
plt.title("Arrival Delay Distribution")
plt.xlabel("Arrival Delay (minutes)")
plt.ylabel("Frequency")
plt.xlim(-50, 300)
plt.tight_layout()
plt.show()
print("Chart displayed: Arrival Delay Distribution.")

print("\nFlight Delay EDA completed.")


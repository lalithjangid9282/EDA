import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
# Ensure 'Sample Superstore.csv' is in the same directory as this script.
# Changed encoding to 'latin-1' to resolve the UnicodeDecodeError.
print("Loading data...")
df = pd.read_csv("../Sample Superstore.csv", encoding='latin-1')
print("Data loaded successfully.")
print("\nInitial Dataset Preview:\n", df.head())

# --- Data Preprocessing ---
print("\nPerforming data preprocessing...")
# Convert 'Order Date' column to datetime objects for time-series analysis
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month and year from the date for later plotting
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year
print("Data preprocessing complete.")

# --- Category-wise Sales & Profit ---
print("\nGenerating Sales and Profit by Category chart...")
# Group by 'Category' to calculate total sales and profit
category_group = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
category_group.plot(kind='bar', figsize=(8, 5), title="Sales & Profit by Category")
plt.tight_layout()
plt.show()
print("Displayed: Sales and Profit by Category")

# --- Region-wise Profit ---
print("\nGenerating Profit by Region chart...")
# Group by 'Region' to calculate total profit
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_profit.plot(kind='barh', color='skyblue', title="Profit by Region")
plt.tight_layout()
plt.show()
print("Displayed: Profit by Region")

# --- Segment-wise Performance ---
print("\nGenerating Sales and Profit by Customer Segment chart...")
# Group by 'Segment' to analyze sales and profit for different customer segments
seg_perf = df.groupby('Segment')[['Sales', 'Profit']].sum()
seg_perf.plot(kind='bar', figsize=(8, 4), title="Sales & Profit by Customer Segment")
plt.tight_layout()
plt.show()
print("Displayed: Sales and Profit by Customer Segment")

# --- Monthly Sales Trend ---
print("\nGenerating Monthly Sales Trend chart...")
# Group by month and year to plot the monthly sales trend over the years
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales.plot(figsize=(12, 5), title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
print("Displayed: Monthly Sales Trend")

# --- Top/Bottom Sub-Categories ---
print("\nGenerating Top/Bottom Sub-Categories chart...")
# Group by 'Sub-Category' and sort by profit to highlight profitable and unprofitable items
subcat = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Profit')
fig, ax = plt.subplots(figsize=(10, 6))
# Use a conditional list comprehension to color bars based on profit (green for profit, red for loss)
subcat['Profit'].plot(kind='barh', ax=ax, color=['red' if p < 0 else 'green' for p in subcat['Profit']])
plt.title("Profit by Sub-Category")
plt.tight_layout()
plt.show()
print("Displayed: Profit by Sub-Category")

# === Done ===
print("\nEDA Completed.")

df.to_csv("Superstore_cleaned.csv", index=False)
print("saved Successfully")

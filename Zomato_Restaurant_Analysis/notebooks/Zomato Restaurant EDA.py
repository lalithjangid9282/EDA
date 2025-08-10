import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Load the dataset
try:
    df = pd.read_csv("../zomato.csv", encoding='latin-1', low_memory=False)
    print("✅ Data loaded successfully!")
    print(f"Dataset shape: {df.shape}")
except FileNotFoundError:
    print("❌ Error: 'zomato.csv' file not found!")
    exit()

print("\nFirst 5 Rows:\n", df.head())
print("\nColumn Names:\n", list(df.columns))
print(f"\nDataset Info:")
print(f"Shape: {df.shape}")
print(f"Memory usage: {df.memory_usage().sum() / 1024**2:.2f} MB")

# Clean the rate column
print("\n🧹 Cleaning rate column...")
if 'rate' in df.columns:
    print(f"Original rate column sample: {df['rate'].value_counts().head()}")
    
    # Remove rows with missing or non-numeric ratings
    initial_count = len(df)
    df = df[df['rate'].notnull()]
    df = df[~df['rate'].astype(str).isin(['NEW', '-', 'nan'])]
    
    # Extract numeric rating from formats like "4.1/5" or "4.1"
    df['rate'] = df['rate'].astype(str).apply(lambda x: x.split('/')[0]).str.strip()
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
    df = df.dropna(subset=['rate'])
    
    final_count = len(df)
    print(f"Removed {initial_count - final_count} rows with invalid ratings")
    print(f"Final dataset shape: {df.shape}")
    print(f"Rate range: {df['rate'].min():.1f} to {df['rate'].max():.1f}")
else:
    print("❌ 'rate' column not found!")

# Plot 1: Top 10 locations with most restaurants
print("\n📊 Creating location analysis...")
if 'location' in df.columns:
    city_count = df['location'].value_counts().head(10)
    
    plt.figure(figsize=(12, 6))
    bars = city_count.plot(kind='bar', color='skyblue', alpha=0.8)
    plt.title("Top 10 City Areas with Most Restaurants", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Restaurants")
    plt.xlabel("Location")
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on bars
    for i, v in enumerate(city_count.values):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    print(f"Top location: {city_count.index[0]} with {city_count.iloc[0]} restaurants")
else:
    print("❌ Column 'location' not found.")

# Plot 2: Distribution of restaurant ratings
print("\n📊 Creating rating distribution...")
if 'rate' in df.columns and len(df) > 0:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['rate'], bins=20, kde=True, color='coral', alpha=0.7)
    plt.title("Distribution of Restaurant Ratings", fontsize=14, fontweight='bold')
    plt.xlabel("Rating")
    plt.ylabel("Count")
    
    # Add statistics
    mean_rating = df['rate'].mean()
    median_rating = df['rate'].median()
    plt.axvline(mean_rating, color='red', linestyle='--', label=f'Mean: {mean_rating:.2f}')
    plt.axvline(median_rating, color='blue', linestyle='--', label=f'Median: {median_rating:.2f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    print(f"Average rating: {mean_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")
else:
    print("❌ Cannot create rating distribution - no valid rate data")

# Plot 3: Top 10 popular cuisines
print("\n📊 Creating cuisine analysis...")
if 'cuisines' in df.columns:
    # Handle NaN values properly
    df_cuisine = df[df['cuisines'].notnull()].copy()
    df_cuisine['cuisines'] = df_cuisine['cuisines'].astype(str)
    
    # Split and explode cuisines
    cuisine_series = df_cuisine['cuisines'].str.split(', ').explode()
    # Remove empty strings and 'nan'
    cuisine_series = cuisine_series[~cuisine_series.isin(['', 'nan', 'None'])]
    top_cuisines = cuisine_series.value_counts().head(10)
    
    plt.figure(figsize=(12, 6))
    bars = top_cuisines.plot(kind='barh', color='lightgreen', alpha=0.8)
    plt.title("Top 10 Popular Cuisines", fontsize=14, fontweight='bold')
    plt.xlabel("Number of Restaurants")
    plt.ylabel("Cuisine Type")
    
    # Add value labels
    for i, v in enumerate(top_cuisines.values):
        plt.text(v + 1, i, str(v), ha='left', va='center')
    
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    print(f"Most popular cuisine: {top_cuisines.index[0]} ({top_cuisines.iloc[0]} restaurants)")
else:
    print("❌ Column 'cuisines' not found.")

# Plot 4: Price vs Rating analysis
print("\n📊 Creating price vs rating analysis...")
price_columns = [col for col in df.columns if 'price' in col.lower() or 'cost' in col.lower()]
print(f"Detected price-related columns: {price_columns}")

if price_columns:
    for col in price_columns:
        try:
            # Clean price column
            df_price = df[df[col].notnull()].copy()
            
            # Try to extract numeric values from price column
            if df_price[col].dtype == 'object':
                # Remove currency symbols and extract numbers
                df_price[col] = df_price[col].astype(str).str.extract(r'(\d+)').astype(float)
            else:
                df_price[col] = pd.to_numeric(df_price[col], errors='coerce')
            
            # Remove outliers (optional)
            Q1 = df_price[col].quantile(0.25)
            Q3 = df_price[col].quantile(0.75)
            IQR = Q3 - Q1
            df_price = df_price[(df_price[col] >= Q1 - 1.5*IQR) & (df_price[col] <= Q3 + 1.5*IQR)]
            
            if len(df_price) > 10:  # Only plot if we have enough data
                plt.figure(figsize=(12, 6))
                sns.boxplot(data=df_price, x=col, y='rate', palette='pastel')
                plt.title(f"{col} vs Rating", fontsize=14, fontweight='bold')
                plt.xlabel(col.title())
                plt.ylabel("Rating")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
                
                # Calculate correlation
                correlation = df_price[col].corr(df_price['rate'])
                print(f"Correlation between {col} and rating: {correlation:.3f}")
                break
            else:
                print(f"⚠️ Not enough valid data for {col}")
                
        except Exception as e:
            print(f"❌ Error plotting boxplot for column {col}: {e}")
else:
    print("ℹ️ No price-related columns found")

# Save cleaned data
try:
    df.to_csv("zomato_cleaned.csv", index=False)
    print(f"\n✅ Cleaned data saved to 'zomato_cleaned.csv'")
    print(f"Saved {len(df)} rows and {len(df.columns)} columns")
except Exception as e:
    print(f"❌ Error saving file: {e}")

# Summary statistics
print(f"\n📈 Analysis Summary:")
print(f"- Total restaurants analyzed: {len(df):,}")
print(f"- Average rating: {df['rate'].mean():.2f}")
print(f"- Rating range: {df['rate'].min():.1f} - {df['rate'].max():.1f}")
if 'location' in df.columns:
    print(f"- Number of unique locations: {df['location'].nunique()}")
if 'cuisines' in df.columns:
    unique_cuisines = len(df['cuisines'].str.split(', ').explode().unique())
    print(f"- Number of unique cuisines: {unique_cuisines}")

print("\n🎉 Analysis completed successfully!")

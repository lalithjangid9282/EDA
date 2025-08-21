import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
print("Loading dataset 'SpotifyFeatures.csv'...")
try:
    df = pd.read_csv("../SpotifyFeatures.csv")
    print("Dataset loaded successfully.")
    print(f"Dataset shape: {df.shape}")
    print(f"Dataset columns: {df.columns.tolist()}")
except FileNotFoundError:
    print("Error: 'SpotifyFeatures.csv' not found. Please ensure the file is in the same directory.")
    exit()

# Drop duplicates or nulls if any
print("\nDropping duplicates and null values...")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print("Duplicates and null values handled. New dataset shape:", df.shape)

# Correlation Matrix
print("\nGenerating Correlation Matrix heatmap...")
plt.figure(figsize=(10, 8))
corr = df[['popularity', 'tempo', 'energy', 'valence', 'loudness', 'danceability']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
print("Displayed: Correlation Matrix heatmap.")

# Average Popularity by Genre
print("\nGenerating Top 10 Genres by Average Popularity chart...")
genre_pop = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_pop.index, y=genre_pop.values, hue=genre_pop.index, palette="viridis", legend=False)
plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Genre")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Displayed: Top 10 Genres by Average Popularity chart.")

# Tempo vs Popularity
print("\nGenerating Tempo vs Popularity scatter plot...")
plt.figure(figsize=(12, 6))
# Using a sample of the data for faster plotting with matplotlib
sns.scatterplot(data=df.sample(n=1000, random_state=1), x='tempo', y='popularity', hue='genre', s=20)
plt.title("Tempo vs Popularity")
plt.xlabel("Tempo")
plt.ylabel("Popularity")
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
print("Displayed: Tempo vs Popularity scatter plot.")

# Energy vs Popularity
print("\nGenerating Energy vs Popularity scatter plot...")
plt.figure(figsize=(12, 6))
# Using a sample of the data for faster plotting with matplotlib
sns.scatterplot(data=df.sample(n=1000, random_state=1), x='energy', y='popularity', hue='genre', s=20)
plt.title("Energy vs Popularity")
plt.xlabel("Energy")
plt.ylabel("Popularity")
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
print("Displayed: Energy vs Popularity scatter plot.")

# Histogram of Tempo
print("\nGenerating Tempo Distribution histogram...")
plt.figure(figsize=(10, 5))
sns.histplot(df['tempo'], bins=50, kde=True, color='purple')
plt.title("Tempo Distribution")
plt.xlabel("Tempo")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
print("Displayed: Tempo Distribution histogram.")

# Histogram of Energy
print("\nGenerating Energy Distribution histogram...")
plt.figure(figsize=(10, 5))
sns.histplot(df['energy'], bins=50, kde=True, color='orange')
plt.title("Energy Distribution")
plt.xlabel("Energy")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
print("Displayed: Energy Distribution histogram.")

# Songs by Year
if 'year' in df.columns:
    print("\nGenerating Songs Released Per Year line plot...")
    year_trend = df['year'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=year_trend.index, y=year_trend.values, marker='o')
    plt.title("Songs Released Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Songs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Displayed: Songs Released Per Year line plot.")

print("\nEDA Completed.")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn style
sns.set(style="darkgrid")
print("Seaborn style set to 'darkgrid'.")

# Load datasets
print("Loading datasets...")
try:
    matches = pd.read_csv("../Matches.csv")
    deliveries = pd.read_csv("../Deliveries.csv")
    print("Datasets loaded successfully.")
except FileNotFoundError:
    print("Error: 'Matches.csv' or 'Deliveries.csv' not found. Please ensure the files are in the same directory.")
    exit()

# View available columns
print("\nMatches Columns:", matches.columns.tolist())
print("Deliveries Columns:", deliveries.columns.tolist())

# Data Cleaning
print("\nStarting data cleaning...")

# Fix: Reassign the DataFrame instead of using inplace=True to avoid FutureWarning
matches['winner'] = matches['winner'].fillna('No Result')

if 'umpire3' in matches.columns:
    # Fix: Drop the column and reassign the DataFrame
    matches = matches.drop(['umpire3'], axis=1)
print("Data cleaning complete. Missing 'winner' values filled, and 'umpire3' column removed if it existed.")

# === Plotting and Analysis ===

# 1. Most Matches Won by Teams
print("\nGenerating Most Matches Won by Teams chart...")
plt.figure(figsize=(12, 6))
wins = matches['winner'].value_counts()
# Fix: Added hue=wins.index and legend=False to address FutureWarning
sns.barplot(x=wins.index, y=wins.values, hue=wins.index, palette="viridis", dodge=False, legend=False)
plt.xticks(rotation=45)
plt.title('Most Matches Won by Teams')
plt.ylabel('Total Wins')
plt.xlabel('Team')
plt.tight_layout()
plt.show()
print("Displayed: Most Matches Won by Teams")

# 2. Win by Runs Distribution
if 'win_by_runs' in matches.columns:
    print("\nGenerating Distribution of Win by Runs chart...")
    plt.figure(figsize=(10, 5))
    sns.histplot(matches['win_by_runs'], bins=30, kde=True, color='orange')
    plt.title('Distribution of Win by Runs')
    plt.xlabel('Win by Runs')
    plt.ylabel('Number of Matches')
    plt.tight_layout()
    plt.show()
    print("Displayed: Distribution of Win by Runs")
else:
    print("\nColumn 'win_by_runs' not found in matches.csv.")

# 3. Win by Wickets Distribution
if 'win_by_wickets' in matches.columns:
    print("\nGenerating Distribution of Win by Wickets chart...")
    plt.figure(figsize=(10, 5))
    sns.histplot(matches['win_by_wickets'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Win by Wickets')
    plt.xlabel('Win by Wickets')
    plt.ylabel('Number of Matches')
    plt.tight_layout()
    plt.show()
    print("Displayed: Distribution of Win by Wickets")
else:
    print("\nColumn 'win_by_wickets' not found in matches.csv.")

# 4. Toss Impact Analysis
if 'toss_winner' in matches.columns and 'winner' in matches.columns:
    toss_match_win = matches[matches['toss_winner'] == matches['winner']]
    toss_win_percent = len(toss_match_win) / len(matches) * 100
    print(f"\nToss Impact: {toss_win_percent:.2f}% of toss winners also won the match.")

    if 'toss_decision' in matches.columns:
        print("\nGenerating Toss Decision Trends chart...")
        plt.figure(figsize=(8, 5))
        sns.countplot(data=matches, x='toss_decision', hue='toss_decision', legend=False)
        plt.title('Toss Decision Trends')
        plt.xlabel('Toss Decision')
        plt.tight_layout()
        plt.show()
        print("Displayed: Toss Decision Trends")

# 5. Top 10 Run Scorers
if 'batsman' in deliveries.columns and 'batsman_runs' in deliveries.columns:
    print("\nGenerating Top 10 Run Scorers chart...")
    top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    # Fix: Added hue=top_scorers.index and legend=False to address FutureWarning
    sns.barplot(x=top_scorers.index, y=top_scorers.values, palette="crest", hue=top_scorers.index, legend=False)
    plt.title("Top 10 Run Scorers")
    plt.ylabel("Total Runs")
    plt.xlabel("Batsman")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Displayed: Top 10 Run Scorers")

# 6. Top 10 Wicket Takers
if 'bowler' in deliveries.columns and 'dismissal_kind' in deliveries.columns:
    print("\nGenerating Top 10 Wicket Takers chart...")
    dismissals = deliveries[deliveries['dismissal_kind'].notnull()]
    top_wickets = dismissals.groupby('bowler').size().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    # Fix: Added hue=top_wickets.index and legend=False to address FutureWarning
    sns.barplot(x=top_wickets.index, y=top_wickets.values, palette="rocket", hue=top_wickets.index, legend=False)
    plt.title("Top 10 Wicket Takers")
    plt.ylabel("Wickets Taken")
    plt.xlabel("Bowler")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Displayed: Top 10 Wicket Takers")

# 7. Matches per Season
if 'season' in matches.columns:
    print("\nGenerating Matches Played Per Season chart...")
    season_count = matches['season'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    # Fix: Added hue=season_count.index and legend=False to address FutureWarning
    sns.barplot(x=season_count.index, y=season_count.values, palette="mako", hue=season_count.index, legend=False)
    plt.title("Matches Played Per Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.tight_layout()
    plt.show()
    print("Displayed: Matches Played Per Season")

# === Done ===
print("\nIPL EDA Completed.")

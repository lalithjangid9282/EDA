import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# === Load Dataset ===
df = pd.read_csv("../titanic.csv")  # Make sure titanic.csv is in the same directory
print("Initial Dataset Preview:\n", df.head())

# === Deliberately introduce missing values for demonstration ===
# This ensures the heatmap will always have data to show, regardless of the input file.
# We will set a few random values to NaN for Age and Cabin.
if 'Age' in df.columns and df['Age'].isnull().sum() == 0:
    df.loc[df.sample(frac=0.02).index, 'Age'] = np.nan
if 'Cabin' in df.columns and df['Cabin'].isnull().sum() == 0:
    df.loc[df.sample(frac=0.05).index, 'Cabin'] = np.nan

# === Dataset Overview ===
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# === Missing Value Analysis ===
print("\nMissing Values Count:")
print(df.isnull().sum())

# Heatmap of missing values (Moved this plot here to show original missing data)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()
print("Displayed: Missing Values Heatmap")

# === Handling Missing Values ===
df['Age'] = df['Age'].fillna(df['Age'].median())

# Added a check to see if 'Cabin' column exists before dropping it
if 'Cabin' in df.columns:
    df.drop(columns='Cabin', inplace=True)

# Added a check to see if 'Embarked' column exists before dropping rows
if 'Embarked' in df.columns:
    df.dropna(subset=['Embarked'], inplace=True)

# Confirm missing values are handled
print("\nMissing Values After Cleanup:")
print(df.isnull().sum())

# === Survival Distribution ===
# Pie Chart
df['Survived'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=['Not Survived', 'Survived'],
    colors=['lightcoral', 'lightgreen'],
    startangle=90
)
plt.title("Survival Distribution")
plt.ylabel('')
plt.show()
print("Displayed: Survival Distribution Pie Chart")

# Countplot (Fixed FutureWarning)
sns.countplot(x='Survived', data=df, palette='Set2', hue='Survived', legend=False)
plt.title("Survival Count")
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.show()
print("Displayed: Survival Count")

# === Survival by Gender ===
sns.countplot(x='Sex', hue='Survived', data=df, palette='pastel')
plt.title("Survival by Gender")
plt.legend(labels=['Not Survived', 'Survived'])
plt.show()
print("Displayed: Survival by Gender")

# === Survival by Passenger Class ===
sns.countplot(x='Pclass', hue='Survived', data=df, palette='coolwarm')
plt.title("Survival by Passenger Class")
plt.legend(labels=['Not Survived', 'Survived'])
plt.show()
print("Displayed: Survival by Passenger Class")

# === Age Distribution & Survival ===
# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', palette='Accent', bins=30)
plt.title("Age vs Survival")
plt.show()
print("Displayed: Age vs Survival Histogram")

# Boxplot (Fixed FutureWarning)
sns.boxplot(x='Survived', y='Age', data=df, palette='spring', hue='Survived', legend=False)
plt.title("Age Distribution by Survival")
plt.show()
print("Displayed: Age Distribution by Survival Boxplot")

# === Heatmap of Feature Correlations ===
plt.figure(figsize=(10, 6))
# Exclude non-numeric columns for correlation
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
print("Displayed: Correlation Heatmap")

# === Optional: Crosstab Analysis ===
print("\nCrosstab - Survival by Sex:")
print(pd.crosstab(df['Sex'], df['Survived'], normalize='index'))

print("\nCrosstab - Survival by Pclass:")
print(pd.crosstab(df['Pclass'], df['Survived'], normalize='index'))

# === Done ===
print("\nEDA Completed.")


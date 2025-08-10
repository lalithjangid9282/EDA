Titanic EDA and Survival Analysis
A detailed exploratory data analysis (EDA) project to understand the factors that influenced the survival of passengers on the Titanic using the classic dataset.

Objective
Explore survival rates and distributions.

Analyze the relationship between survival and passenger attributes like gender, age, and class.

Visualize the data to identify key trends and correlations.

Clean and preprocess the dataset for analysis.

Dataset
titanic.csv

Tools Used
Python: pandas, matplotlib, seaborn, numpy

Key Findings
Females had a significantly higher survival rate than males.

Passengers in first class had a much higher chance of survival compared to those in lower classes.

Younger passengers and children showed a higher survival rate.

Age, Passenger Class (Pclass), and Gender (Sex) are key features correlated with survival.

Visualizations Included
Pie chart and countplot of survival distribution.

Countplot of survival by gender and passenger class.

Histogram of age distribution and survival.

Boxplot of age distribution by survival.

Heatmap of feature correlations.

Heatmap of missing values in the original dataset.

How to Run the Analysis
Prerequisites
You will need Python installed on your system.

First, make sure all the required Python libraries are installed:

pip install pandas seaborn matplotlib numpy

Execution
To run the script, ensure titanic.csv is in the same directory as your Python file (e.g., titanic_eda.py). Then, simply execute the script from your terminal:

python titanic_eda.py

The script will print outputs to the console and display the plots in separate windows.

File Structure
├── titanic_eda.py
├── titanic.csv
├── titanic_cleaned.csv
├── README.md
└── .gitignore
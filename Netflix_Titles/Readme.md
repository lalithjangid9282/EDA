Netflix Titles Exploratory Data Analysis
A detailed exploratory data analysis (EDA) project to understand trends in genres, release years, and content duration on the Netflix platform using the Netflix Titles dataset.

Objective
Explore content distribution by genre and country.

Analyze the trend of content releases over the years.

Understand the distribution of content duration for movies and TV shows.

Create an interactive dashboard for a user-friendly experience.

Dataset
netflix_titles.csv

Tools Used
Python: pandas, matplotlib, seaborn, plotly

Streamlit: for live interactive deployment

Key Findings
The number of titles released has grown significantly over the years.

The most common genres include Dramas, Comedies, and Documentaries.

The United States is the country with the highest number of titles.

Most movies are between 90 and 120 minutes long.

Visualizations Included
Bar chart of top 10 genres.

Line plot of content release trend by year.

Bar chart of top 10 countries by content count.

Histogram of movie duration distribution.

Histogram of TV show season distribution.

How to Run the Streamlit App
git clone https://github.com/yourusername/your-netflix-project.git
cd your-netflix-project
pip install -r requirements.txt
streamlit run app.py

File Structure
├── app.py
├── netflix_titles.csv
├── netflix_cleaned.csv
├── README.md
└── requirements.txt
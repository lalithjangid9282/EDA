Spotify Data Analysis Project
An exploratory data analysis (EDA) project to analyze a dataset of Spotify songs, exploring the relationships between song features and popularity.

Objective
Examine the correlation between various song attributes (e.g., tempo, energy, danceability) and popularity.

Identify the most popular music genres.

Visualize the distribution of key audio features like tempo and energy.

Analyze trends in the number of songs released over the years.

Dataset
SpotifyFeatures.csv

Tools Used
Python: pandas, seaborn, matplotlib

Streamlit (for the interactive dashboard)

Visualizations Included
A correlation matrix heatmap of key song features.

A bar chart showing the average popularity of the top 10 genres.

Scatter plots illustrating the relationship between tempo/energy and popularity.

Histograms showing the distribution of tempo and energy.

A line plot displaying the number of songs released per year.

How to Run the Analysis
Prerequisites
You will need Python installed on your system.
Install the required Python libraries using pip:

pip install -r requirements.txt

Execution
To run the analysis script, ensure SpotifyFeatures.csv is in the same directory as your Python file (spotify_eda.py). Then, execute the script from your terminal:

python spotify_eda.py

To run the interactive Streamlit dashboard, use the following command:

streamlit run Spotify_app.py

The Streamlit app will open in your default web browser.

File Structure
├── spotify_eda.py
├── Spotify_app.py
├── SpotifyFeatures.csv
├── requirements.txt
├── .gitignore
└── README.md

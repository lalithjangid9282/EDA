Airbnb NYC Data Analysis Project
An exploratory data analysis (EDA) project to analyze Airbnb listings in New York City using a public dataset from 2019. The analysis covers price, room types, geographical distribution, and availability.

Objective
Understand the distribution of listing prices, focusing on listings under $500.

Analyze the distribution of different room types (e.g., Entire home/apt, Private room).

Examine the number of listings and average price per borough (neighbourhood_group).

Visualize the availability of listings throughout the year.

Create a geospatial heatmap to identify clusters of listings in NYC.

Dataset
AB_NYC_2019.csv

Tools Used
Python: pandas, seaborn, matplotlib, folium

Visualizations Included
Histogram of price distribution.

Bar chart of room type counts.

Bar chart of listings by borough.

Bar chart of average price by borough.

Histogram of listing availability.

Interactive Folium map with a heatmap of listing locations.

How to Run the Analysis
Prerequisites
You will need Python installed on your system.
Install the required Python libraries using pip:

pip install -r requirements.txt

Execution
To run the script, ensure AB_NYC_2019.csv is in the same directory as your Python file. Then, execute the script from your terminal:

python airbnb_eda.py

The script will display the plots in separate windows and save the interactive map as nyc_airbnb_map.html in the same directory.

File Structure
├── airbnb_eda.py
├── AB_NYC_2019.csv
├── nyc_airbnb_map.html
├── requirements.txt
├── .gitignore
└── README.md

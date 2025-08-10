Uber Data Analysis Project
An exploratory data analysis (EDA) project to understand the trip patterns of Uber pickups in New York City based on time and location data.

Objective
Analyze trip frequency by hour of the day and day of the week.

Visualize pickup hotspots using a geospatial heatmap.

Identify popular pickup times and days.

Dataset
Uber_Data.csv

Tools Used
Python: pandas, seaborn, matplotlib, folium

Visualizations Included
Bar chart of hourly trip frequency.

Bar chart of trip frequency by day of the week.

Heatmap showing the distribution of trips across hours and days.

Interactive geospatial heatmap of pickup locations in NYC.

How to Run the Analysis
Prerequisites
You will need Python installed on your system.
Install the required Python libraries using pip:

pip install pandas seaborn matplotlib folium

Execution
To run the script, ensure Uber_Data.csv is in the same directory as your Python file (e.g., uber_eda.py). Then, execute the script from your terminal:

python uber_eda.py

The script will print outputs to the console and display the plots in separate windows. The interactive Folium map will be generated and can be saved as an HTML file if you uncomment the pickup_map.save() line in the script.

File Structure
├── uber_eda.py
├── Uber_Data.csv
├── hourly_trips.png (Optional)
├── weekday_trips.png (Optional)
├── hour_vs_weekday_heatmap.png (Optional)
├── nyc_pickup_map.html (Optional)
├── uber_app.py (Optional)
├── requirements.txt (Optional)
└── README.md

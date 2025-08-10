Flight Delay and Cancellation Data Analysis
A data analysis project to explore flight delays and cancellations using a sample dataset from 2019-2023. This analysis identifies key trends and factors contributing to flight delays.

Objective
Analyze average arrival delays by airline.

Identify the primary causes of flight delays.

Examine monthly trends in flight delays.

Find the most delayed flight routes.

Dataset
flights_sample_3m.csv

The dataset contains flight information including departure and arrival times, delay reasons, and route details.

Tools Used
Python: pandas for data manipulation, seaborn and matplotlib for data visualization.

Streamlit: for creating an interactive web dashboard (Flight_app.py).

Key Findings
The analysis shows a significant variation in average arrival delays across different airlines.

The most common causes of delays are often related to carrier issues and late aircraft, followed by weather and National Air System (NAS) delays.

Flight delays show seasonal trends, with certain months experiencing higher average delays.

The analysis highlights specific routes that are consistently among the most delayed.

File Structure
.
├── Flight_app.py
├── flights_sample_3m.csv
├── requirements.txt
├── .gitignore
└── README.md

How to Run the Project
Prerequisites
Ensure you have Python installed.

Install the necessary libraries by running:

pip install -r requirements.txt

Download the flights_sample_3m.csv file from the Kaggle dataset link and place it in the same directory as the Python scripts.

Execution
To run the Streamlit dashboard, execute the following command in your terminal:

streamlit run Flight_app.py

This will start a local web server and open the dashboard in your default browser.
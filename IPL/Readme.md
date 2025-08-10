IPL Data Analysis Project

An exploratory data analysis (EDA) project to analyze various aspects of Indian Premier League (IPL) matches, including team performance, player statistics, and match trends.



Objective

Identify the most successful teams in terms of match wins.



Analyze the distribution of winning margins (by runs and wickets).



Investigate the impact of winning the toss on the match outcome.



Highlight the top batsmen and bowlers in the league.



Understand the number of matches played per season.



Dataset

Matches.csv: Contains match-level information (e.g., teams, venue, winner).



Deliveries.csv: Contains ball-by-ball details for all matches.



Tools Used

Python: pandas, seaborn, matplotlib



Key Findings

Toss Impact: The analysis shows that winning the toss has a significant correlation with winning the match.



Top Performers: The charts reveal the leading teams in total wins, and the top 10 batsmen and bowlers in the league's history.



Match Trends: The data provides insights into win margins and the number of matches played across different seasons.



Visualizations Included

Bar chart of total matches won by each team.



Histograms showing the distribution of wins by runs and wickets.



Count plot for toss decision trends.



Bar chart of the top 10 run scorers.



Bar chart of the top 10 wicket takers.



Bar chart showing the number of matches played per season.



How to Run the Analysis

Prerequisites

You will need Python installed on your system.

Install the required Python libraries using pip:



pip install pandas seaborn matplotlib



Execution

The script is now designed to be self-sufficient. It will automatically download the necessary CSV files if they are not already present in the same directory.



Simply execute the script from your terminal:



python ipl\_eda.py



The script will handle the data download, print outputs to the console, and display the plots in separate windows.



File Structure

├── ipl\_eda.py

├── Matches.csv

├── Deliveries.csv

├── .gitignore

└── README.md




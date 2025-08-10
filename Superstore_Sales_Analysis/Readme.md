 Superstore Sales Analysis 
A comprehensive sales and profit analysis using the Superstore dataset. The 
project explores patterns across product categories, regions, customer segments, 
and seasonal trends. 
# Objective - Understandsales and profit  performance by **category, region, and customer segment - Identify seasonal patterns*in sales - Create pivot tables and dashboards for business insights 
# Dataset - Source: [Superstore Dataset – Kaggle](https://www.kaggle.com/datasets/vivek468/superstore
dataset-final) 
FileSuperstore.csv` - Attributes: Order Date, Ship Mode, Segment, Country, Category, Sub-Category, Sales, Profit, 
Region, etc. 

# Tools Used - Excel: Pivot tables, summary charts -Power BI: Interactive dashboards - Python: Data wrangling & EDA with Pandas/Matplotlib 
## Key Analysis Areas - Category-wise **sales & profit breakdown** - Region and segment-based performance - **Seasonality** in sales (month/year trends) - Top & bottom performing sub-categories 
#Visualizations Include - Heatmap of profit by category and region - Line plot of monthly sales trends - Bar charts for sales/profit by segment - Power BI dashboard with slicers 

##  How to Use 
# Clone the repo 
git clone https://github.com/yourusername/superstore-sales-analysis.git 
cd superstore-sales-analysis 
# Run Python EDA script 
pip install -r requirements.txt 
python superstore_eda.py 
Project Structure 
├── data/ 
│   └── Superstore.csv 
├── superstore_eda.py 
├── superstore_powerbi.pbix 
├── Excel_Pivot_Analysis.xlsx 
├── README.md 
└── requirements.txt
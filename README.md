# 👨🏻‍💻 End-to-End Data Analytics Project
This project represents a complete, industry standard, end-to-end data analytics workflow, designed to mirror the real responsibilities of professional analysts in modern business environments. The project encompasses all critical stages of data analysis, from data preparation and modeling to insight generation, visualization, and reporting.
A complete analytics workflow: Python (loading and cleaning) → SQL (business queries) → Power BI (dashboard) → Report → Presentation.

# Project Overview
This project analyzes **customer_shopping_behavior** to answer key business questions such as:

- What are the main trends over time?
- Which categories, regions, or customers drive the most value?
- What actions can the business take based on the data?

The project covers the full analytics lifecycle, from raw data to a decision-ready dashboard, written report, and presentation.

# Dataset
 -**Source**  - public URL
 -**Rows × Columns**  3,900 × 18
 -**File Format**  CSV / Excel 

# Key columns
-**Customer ID**	Identify customers and analyze purchasing behavior
-**Category**	Identify the most popular product categories
-**Purchase Amount** (USD)	Analyze spending and revenue
-**Review Rating**	Measure customer satisfaction

# Tools
-**Python (Pandas, NumPy)** Data loading and cleaning
-**PostgreSQL** Querying and analysis
-**Power BI** Dashboard
-**Word / PDF** Reporting
-**Gamma** Presentation
**Git and GitHub** Version control

---
## Steps

### 1. Data Loading (Python)
- Loaded the dataset into a Pandas DataFrame
- Checked shape, data types, and a sample of records

### 2. Data Cleaning
- Handled missing values and duplicates
- Fixed data types and inconsistent formatting
- Treated outliers and created derived columns (e.g., month, revenue)
- Exported the cleaned dataset for SQL and Power BI

### 3. SQL Analysis
- Loaded the cleaned data into **PostgreSQL**
- Wrote queries using `JOIN`, `GROUP BY`, CTEs, subqueries, and window functions
- Answered business questions such as top products, monthly trends, and customer segments

### 4. Power BI Dashboard
- Connected Power BI to the cleaned data / SQL database
- Built interactive visuals with slicers and KPI cards
- Added DAX measures for calculated metrics

### 5. Report
- Documented the approach, insights, and recommendations

### 6. Presentation
- Created a concise slide deck using **Gamma** for stakeholders

---

## Dashboard

![Dashboard Preview](images/dashboard.png)

## How to Run

### Prerequisites
- Python 3.9+
- PostgreSQL
- Power BI Desktop

### Setup
# 1. Clone the repository
git clone https://github.com/vedavalliguntuku/End-to-End Data Analytics Project.git
cd End-to-End Data Analytics Project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the cleaning
Customer_Shopping_Behavior.ipynb

### Run the SQL queries
1. Create a database and import `Customer_shopping_behavior.csv`
2. Run the scripts in the `sql/` folder

### Open the dashboard
1. Open `Customer_Shopping_Behavior.pbix` in Power BI Desktop
2. Update the data source path or connection if prompted
3. Click **Refresh**

---

## Project Structure

├── data/              # Raw and cleaned datasets
├── visual studio         # Python loading and cleaning
├── sql/               # SQL queries
├── dashboard/         # Power BI (.pbix) file
├── report/            # Project report
├── presentation/      # Gamma presentation / PDF
├── images/            # Screenshots
├── requirements.txt
└── README.md

## Author

**Vedavalli Guntuku**  
Data Analyst  

🔗 [GitHub](https://github.com/vedavalliguntuku)  
📁 [Project Repository](https://github.com/vedavalliguntuku/End-to-End-Data-Analytics-Project)

⭐ If you found this project helpful, feel free to star the repository!

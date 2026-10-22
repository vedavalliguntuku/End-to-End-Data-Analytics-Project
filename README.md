# Customer Shopping Behavior Analysis: End-to-End Data Analytics Project

> Python (clean and prepare) → SQL (10 business queries) → Power BI (dashboard) → Report → Presentation

**Key result:** analysed 3,900 retail purchases (USD 233K revenue). Male customers bring in 68% of revenue simply because
they are 68% of customers, since spend per purchase is almost identical across genders (about $60). Subscribers spend
no more than non-subscribers, so the subscription programme is a growth opportunity rather than a proven driver of spend.

---

## Overview

A retail company wants to understand its customers' shopping behaviour to improve sales, satisfaction and loyalty.
This project cleans the raw customer data, analyses it with SQL, and presents the findings in an interactive Power BI
dashboard. The business problem is described in [`Business_Problem_Document.pdf`](Business_Problem_Document.pdf).

**Questions answered:**
- Which customer groups (gender, age, subscribers) generate the most revenue?
- Do discounts, shipping type or subscriptions change how much customers spend?
- Which products are rated highest and discounted most?
- How loyal are customers, and are repeat buyers more likely to subscribe?

---

## Dataset

| Item | Details |
|------|---------|
| **File** | `customer_shopping_behavior.csv` |
| **Size** | 3,900 purchases × 18 columns |
| **Currency** | US dollars |
| **Missing data** | 37 values in `Review Rating` (about 1%) |

**Key columns:** `Customer ID`, `Age`, `Gender`, `Item Purchased`, `Category`, `Purchase Amount (USD)`, `Location`,
`Season`, `Review Rating`, `Subscription Status`, `Shipping Type`, `Discount Applied`, `Previous Purchases`,
`Payment Method`, `Frequency of Purchases`

---

## Tools

| Purpose | Tools |
|---------|-------|
| Data loading and cleaning | Python (Pandas) |
| Data storage and analysis | PostgreSQL (loader also supports MySQL and SQL Server) |
| Dashboard | Power BI |
| Reporting | PDF report |
| Presentation | Gamma (PowerPoint export) |

---

## Steps

### 1. Data preparation (Python): [`Customer_Shopping_Behavior.py`](Customer_Shopping_Behavior.py)
- Loaded the CSV and checked structure, summary statistics and missing values
- Filled the 37 missing review ratings with the **median rating of each product category**
- Converted column names to `snake_case`
- Created `age_group` (4 quartile bands) and `purchase_frequency_days`
- Found that `promo_code_used` is identical to `discount_applied` and dropped it
- Loaded the cleaned table into the database

### 2. SQL analysis: [`Customer_Shopping_Behavior.sql`](Customer_Shopping_Behavior.sql)
Ten business questions answered with aggregation, subqueries, `CASE`, CTEs and window functions (`ROW_NUMBER`).

### 3. Power BI dashboard: [`Customer_Shopping_Behavior.pbix`](Customer_Shopping_Behavior.pbix)
Interactive dashboard with slicers for subscription status, gender, category and shipping type.

### 4. Report and presentation
- [`Customer_Shopping_Behavior.pdf`](Customer_Shopping_Behavior.pdf): project report
- [`Customer-Shopping-Behavior.pptx`](Customer-Shopping-Behavior.pptx): stakeholder presentation

---

## Dashboard

![Customer Behaviour Dashboard](Dashboard.png)

- **KPI cards:** 3.9K customers · $59.76 average purchase · 3.75 average review rating
- **Subscription split:** 27% subscribers vs 73% non-subscribers
- **Revenue and sales by category** and **by age group**
- **Slicers:** subscription status, gender, category, shipping type

---

## Results

| Metric | Value |
|--------|------:|
| Total revenue | $233,081 |
| Purchases / customers | 3,900 |
| Average purchase amount | $59.76 |
| Average review rating | 3.75 / 5 |

### Key insights

| # | Question | Finding |
|---|----------|---------|
| 1 | Revenue by gender | Male $157,890 (68%) vs Female $75,191 (32%). Males are 2,652 of 3,900 customers, and average spend is nearly the same ($59.54 vs $60.25), so the gap comes from customer count. |
| 2 | Discount users spending above average | 839 customers used a discount and still spent at or above the average purchase. Discounts are used on 43% of purchases, with no lift in spend ($59.28 with vs $60.13 without). |
| 3 | Top-rated products | Gloves (3.86), Sandals (3.84), Boots (3.82), Hat (3.80), Handbag/Skirt (3.78). |
| 4 | Shipping | Express averages $60.48 vs $58.46 for Standard (+3.5%), a small difference. |
| 5 | Subscribers vs non-subscribers | 1,053 subscribers (27%) generate $62.6K (27% of revenue). Average spend is the same ($59.49 vs $59.87). |
| 6 | Most discounted products | Hat (50.0%), Sneakers (49.7%), Coat (49.1%), Sweater (48.2%), Pants (47.4%). |
| 7 | Customer segments | Loyal 3,116 (80%) · Returning 701 (18%) · New 83 (2%), using thresholds of 11+, 2–10 and 1 previous purchases. |
| 8 | Top products per category | Most ordered: Jewelry (Accessories), Blouse and Pants tied (Clothing), Sandals (Footwear), Jacket (Outerwear). |
| 9 | Repeat buyers and subscriptions | Only 27.6% of repeat buyers (more than 5 purchases) subscribe, about the same as the overall 27.0%. |
| 10 | Revenue by age group | Young adult $62.1K, middle age $59.2K, adult $56.0K, senior $55.8K. Revenue is spread fairly evenly. |

Revenue by category: Clothing $104K (45%), Accessories $74K (32%), Footwear $36K (15%), Outerwear $19K (8%).

### Recommendations
- **Grow subscriptions.** Only 27% of customers subscribe and subscribers do not spend more yet, so add real
  subscriber benefits (early access, free shipping) and test whether they lift spend.
- **Review the discount policy.** Discounts do not raise spend per purchase, so test targeted offers instead of
  blanket discounts, especially on the most-discounted items.
- **Win more female customers.** They spend as much per purchase as male customers but make up only 32% of the base.
- **Redefine the loyalty segments.** With 80% of customers labelled "Loyal", the tiers do not separate anyone; use
  tighter thresholds (for example quartiles of previous purchases).
- **Feature top-rated products** (Gloves, Sandals, Boots) in campaigns.

---

## How to Run

### Prerequisites
- Python 3.9+ and `pip install pandas`
- PostgreSQL (or MySQL / SQL Server) to run the SQL; Power BI Desktop to open the dashboard

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/vedavalliguntuku/end-to-end-data-analytics-project.git
cd end-to-end-data-analytics-project

# 2. Clean the data (creates customer_shopping_behavior_cleaned.csv)
python Customer_Shopping_Behavior.py

# 3. (Optional) also load it into a database as table "customer"
pip install sqlalchemy psycopg2-binary
DB_URL="postgresql+psycopg2://user:password@localhost:5432/customer_behavior" python Customer_Shopping_Behavior.py
```

Then run the queries in `Customer_Shopping_Behavior.sql` in your SQL client, and open
`Customer_Shopping_Behavior.pbix` in Power BI Desktop (update the data source if prompted).

---

## Repository Contents

```
├── customer_shopping_behavior.csv      # raw dataset
├── Customer_Shopping_Behavior.py       # data cleaning and database loading
├── Customer_Shopping_Behavior.sql      # 10 business queries
├── Customer_Shopping_Behavior.pbix     # Power BI dashboard
├── Dashboard.png                       # dashboard screenshot
├── Customer_Shopping_Behavior.pdf      # project report
├── Customer-Shopping-Behavior.pptx     # presentation
├── Business_Problem_Document.pdf       # project brief
└── README.md
```

---

## Author

**Vedavalli Guntuku**, Data Analyst
🔗 [GitHub](https://github.com/vedavalliguntuku) · [LinkedIn](https://www.linkedin.com/in/vedavalliguntuku/)

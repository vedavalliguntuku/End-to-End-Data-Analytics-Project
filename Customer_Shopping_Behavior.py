import pandas as pd
df = pd.read_csv('customer_shopping_behavior.csv')
print(df.head())
df.info()
print(df.describe(include='all'))
print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
print(df.columns)
df = df.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})
print(df.columns)

#create a column age group
labels = ['young adult', 'adult','middle age','senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
print(df[['age', 'age_group']].head(10))

# create new column purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())

#Dropping promo code used column

df = df.drop('promo_code_used', axis=1)
print(df.columns)


#1...!pip install psycopg2-binary sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    "postgresql+psycopg2",
username="postgres",
    password="your_password_here",
    host="localhost",
    port=5432,
    database="customer_shopping_behavior",
)

df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
result = pd.read_sql("SELECT * FROM customer LIMIT 5;", engine)
print(result)

#2...pip install pymysql cryptography
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Load the CSV and standardise column names
df = pd.read_csv("customer_shopping_behavior.csv")
df.columns = df.columns.str.lower().str.replace(" ", "_")

# (cleaning steps here, e.g. df = df.drop('promo_code_used', axis=1))

# 2. MySQL connection

url = URL.create(
    "mysql+pymysql",
    username="root",
    password="your_password_here",
    host="localhost",
    port=3306,
    database="customer_behavior",
)
engine = create_engine(url)

# 3. Write to MySQL
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database 'customer_behavior'.")

# 4. Read back a sample
result = pd.read_sql("SELECT * FROM customer LIMIT 5;", engine)
print(result)

#3...!pip install pyodbc sqlalchemy 
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 1. Load the data (change the file name to match your CSV exactly)
df = pd.read_csv("customer_shopping_data.csv")

# 2. SQL Server connection
url = URL.create(
    "mssql+pyodbc",
    username="sa",
    password="your_password_here",
    host="localhost",
    port=1433,
    database="customer_behavior",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)
engine = create_engine(url)

# 3. Write the DataFrame to SQL Server
df.to_sql("customer", engine, if_exists="replace", index=False)
print("Data loaded into table 'customer'.")

# 4. Read back a sample (SQL Server uses TOP instead of LIMIT)
result = pd.read_sql("SELECT TOP 5 * FROM customer;", engine)
print(result)
df = pd.read_csv("customer_shopping_behavior.csv")





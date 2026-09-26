"""
Task 2 - Exploratory Data Analysis (EDA)
Project: E-Commerce Sales Analysis

Run:
    pip install pandas numpy matplotlib seaborn scipy jupyter
    python eda_analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/ecommerce_sales.csv")
print("Original shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nStatistical summary:\n", df.describe(include="all"))

# Cleaning
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Discount_Percent"] = df["Discount_Percent"].fillna(df["Discount_Percent"].median())
df = df.drop_duplicates().reset_index(drop=True)
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# Analysis
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
monthly_sales = df.groupby("Month")["Sales"].sum()
payment_counts = df["Payment_Method"].value_counts()

print("\nTotal sales:", df["Sales"].sum())
print("Average order value:", df["Sales"].mean())
print("\nSales by category:\n", category_sales)
print("\nTop 10 products:\n", product_sales.head(10))
print("\nSales by city:\n", city_sales)
print("\nPayment method counts:\n", payment_counts)

# Save summary
summary = pd.DataFrame({
    "Metric": [
        "Rows after cleaning", "Total Sales", "Average Order Value",
        "Top Category", "Top City", "Top Product", "Most Used Payment Method"
    ],
    "Value": [
        len(df), round(df["Sales"].sum(), 2), round(df["Sales"].mean(), 2),
        category_sales.index[0], city_sales.index[0], product_sales.index[0],
        payment_counts.index[0]
    ]
})
summary.to_csv("analysis_summary.csv", index=False)
print("\nAnalysis complete. Summary saved as analysis_summary.csv")

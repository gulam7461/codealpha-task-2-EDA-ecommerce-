# CodeAlpha Task 2 — Exploratory Data Analysis

## Project Title
**E-Commerce Sales Analysis**

### Internship
CodeAlpha — Data Analytics

### Task
Task 2: Exploratory Data Analysis (EDA)

## Project Objective
The project explores an e-commerce sales dataset to understand its structure, clean basic data-quality issues, identify trends and patterns, check possible anomalies, and perform a simple statistical test.

## Work completed
- Data loading
- Data structure and data-type checking
- Missing-value analysis
- Duplicate detection and removal
- Data cleaning
- Descriptive statistics
- Category-wise sales analysis
- Product-wise sales analysis
- City-wise sales analysis
- Monthly sales trend
- Payment-method analysis
- IQR-based outlier detection
- Correlation analysis
- ANOVA hypothesis testing
- Charts and written findings

## Tools
Python, Pandas, NumPy, Matplotlib, SciPy and Jupyter Notebook.

## Folder structure
```text
CodeAlpha_Task2_EDA_Final/
├── dataset/
│   └── ecommerce_sales.csv
├── notebook/
│   └── Task_2_EDA_Ecommerce.ipynb
├── visualizations/
│   ├── 01_category_sales.png
│   ├── 02_monthly_sales.png
│   ├── 03_top_products.png
│   ├── 04_city_sales.png
│   ├── 05_payment_methods.png
│   ├── 06_quantity_distribution.png
│   ├── 07_sales_boxplot.png
│   └── 08_correlation_heatmap.png
├── report/
│   └── Task_2_EDA_Report.pdf
├── eda_analysis.py
├── requirements.txt
└── README.md
```

## Dataset note
The included CSV is a synthetic/demo dataset created for learning and internship demonstration. It is not real company or customer data.

## Run the project
```bash
pip install -r requirements.txt
jupyter notebook
```

Then open:
`notebook/Task_2_EDA_Ecommerce.ipynb`

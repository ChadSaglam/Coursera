# Online Retail Exploratory Data Analysis

## Overview
This project involves exploratory data analysis (EDA) on transactional data from an online retail store. The goal is to uncover meaningful business insights related to sales trends, customer behavior, and popular products through data visualization and statistical summaries. These insights can help optimize store operations and improve customer satisfaction.

---

## Dataset
- The dataset used is the **Online Retail** dataset, covering transactions from 2010 to 2011.
- Contains transaction details including:
  - InvoiceNo: Invoice number of the transaction
  - StockCode: Product unique code
  - Description: Product description
  - Quantity: Number of products purchased in a transaction
  - InvoiceDate: Date and time of transaction
  - UnitPrice: Price per unit
  - CustomerID: Unique customer identifier
  - Country: Location of purchase

---

## Prerequisites
This analysis requires Python with the following packages:
- pandas
- numpy
- matplotlib
- seaborn

You can install these packages via pip if not already installed:
```
pip install pandas numpy matplotlib seaborn
```

---

## Project Tasks
The project was divided into the following main tasks:

### 1. Load the Dataset
- Load the Excel data file into a Pandas DataFrame.
- Display the first few rows and structure of the data.

### 2. Data Cleaning
- Handle missing CustomerID values by removing such rows.
- Remove entries with zero or negative quantities (likely returns or errors).

### 3. Basic Statistics
- Generate descriptive statistics to understand data distribution like mean, median, standard deviation, min, and max for key numerical fields.

### 4. Data Visualization
- Create plots such as histograms, scatter plots, and bar charts to visualize quantity distribution, unit price relationships, and more.

### 5. Sales Trend Analysis
- Analyze sales over time, identifying busiest months and weekdays.

### 6. Top Products and Countries
- Identify and visualize top-selling products and countries based on quantity sold.

### 7. Outliers and Anomalies
- Detect extreme values in quantity and price.
- Use boxplots to visualize outliers and discuss their impact.

### 8. Conclusions
- Summarize key findings including total transactions, top customers, best-selling products, and countries.

---

## How to Run
1. Place the file `Online Retail.xlsx` in your working directory.
2. Run the provided Python script or Jupyter notebook with all the analysis code.
3. Visualizations and printed summaries will be generated to assist insight gathering.

---

## Key Insights and Impact
- Identified seasonality and monthly sales peaks.
- Highlighted most valuable products and customer locations.
- Detected potential data quality issues through outlier analysis.
- Insights can guide inventory management, marketing focus, and customer engagement strategies.

---

## Author
This project was developed as a portfolio piece to demonstrate data analysis skills using Python.

---

## License
This project is for educational purposes only; no specific license.

README - Retail Sales Analysis Project
======================================

Project Overview:
-----------------
This project analyzes a retail sales dataset from Kaggle:
https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset/data

The goal is to explore transaction patterns, revenue distribution, and customer behavior across product categories and demographics, and to provide actionable insights.

Project Structure:
-----------------
1. **Python Scripts:**
   - `retail_sales_cleaning.py`   : Data cleaning and preprocessing.
   - `retail_sales_analysis.py`   : Data aggregation, calculations, and statistical analysis.
   - `retail_sales_graphs.py`     : Generation of all visualizations (histograms, bar charts, quartile analysis, etc.)

2. **Figures Directory (`retail_sales_figures`):**
   - Contains all generated figures, organized into subdirectories:
       - `demographic/` : Gender-based and customer segment visualizations.
       - `category/`    : Product category analysis figures.
       - `revenue/`     : Revenue and quartile analysis figures.
   - Includes descriptive statistics tables exported from Python.

3. **Report:**
   - `retail_sales_report.docx` : Full written analysis with all insights, tables, and figures.
   - `retail_sales_report.pdf`  : PDF version for sharing and presentation.

Key Insights:
-------------
- Purchases are right-skewed, with a small number of high-value transactions driving most revenue.
- Electronics and Clothing dominate revenue, with Beauty peaking seasonally.
- Gender-based purchasing patterns highlight opportunities for targeted marketing.
- Quartile analysis shows the fourth quartile contributes disproportionately to total revenue.

Usage Instructions:
-------------------
1. Run the Python scripts in the order:
   - `retail_sales_cleaning.py` → `retail_sales_analysis.py` → `retail_sales_graphs.py`
2. Figures will be saved automatically in the `retail_sales_figures` directory.
3. Review the Word or PDF report for full narrative analysis and recommendations.

Author / Contact:
-----------------
Prepared by: Amr Qeshta  
Date of Completion: February 7th, 2026


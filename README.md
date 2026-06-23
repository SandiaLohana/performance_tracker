📊 AI Model Performance Analyzer

A lightweight Python tool for analyzing and visualizing AI model evaluation results from a CSV file.
It automates data cleaning, statistical analysis, and visual comparison of multiple machine learning models.

🧠 Overview

This script reads a dataset of AI model performance metrics and generates:

- Cleaned and validated data
- Statistical summaries
- Comparative visualizations using bar charts

It is designed for beginners learning data analysis with Python.

⚙️ Workflow
CSV File → Load Data → Clean Missing Values → Compute Statistics → Visualize Results

📁 Input Format

Your dataset should follow this structure:

Model,Accuracy,Precision,Recall,F1_Score
Model A,0.91,0.89,0.87,0.88
Model B,0.93,0.91,0.90,0.90

📌 What the Script Does
1. Data Loading

Reads ai_models.csv using Pandas.

2. Data Cleaning

Handles missing values using median imputation.

3. Statistical Analysis

Computes:

Mean
Median
Standard Deviation

for each metric.

4. Visualization

Generates bar charts for:

Accuracy
Precision
Recall
F1 Score

📊 Sample Output

After running the script, you will see results like:

Original Dataset:
Model A | Accuracy: 0.91 | Precision: 0.89 | Recall: 0.87 | F1: 0.88
Model B | Accuracy: 0.93 | Precision: 0.91 | Recall: 0.90 | F1: 0.90

Missing Values:
All columns contain 0 missing values

Dataset Statistics:
Mean Accuracy: 0.905
Mean Precision: 0.8825
Mean Recall: 0.8675
Mean F1 Score: 0.8725

📈 Visualization Output

The script generates separate bar charts comparing all models across:

Accuracy
Precision
Recall
F1 Score

Each chart clearly shows performance differences between models.

🧪 Requirements
Python 3.x
pandas
matplotlib

Install dependencies:

pip install pandas matplotlib

🚀 How to Run
python performance_tracker.py

Make sure ai_models.csv is in the same directory.

💡 Key Learning

This project helps you understand:

Data preprocessing in Python
Handling missing values
Basic statistical analysis
Data visualization techniques
Comparing ML model performance

🔮 Possible Improvements
Save charts as image files automatically
Add interactive plots (Plotly / Seaborn upgrade)
Export summary report as PDF
Build a Streamlit dashboard version

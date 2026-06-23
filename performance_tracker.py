#performance_tracker.py

# Expected CSV Format:
# Model,Accuracy,Precision,Recall,F1_Score
# Model A,0.91,0.89,0.87,0.88
# Model B,0.93,0.91,0.90,0.90
# Model C,0.88,0.85,0.84,0.84
# Model D,0.90,0.88,0.86,0.87

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
dataframe = pd.read_csv("ai_models.csv")

# Display the original dataset
print("Original Dataset")
print(dataframe)

# Check for missing values
print("\nMissing Values Before Handling")
print(dataframe.isnull().sum())

# Handle missing values by replacing them with the median
dataframe = dataframe.fillna(dataframe.median(numeric_only=True))

# Display dataset information
print("\nDataset Information")
dataframe.info()

# Display basic statistical summary
print("\nDataset Statistics")
print(dataframe.describe())

# List of performance metrics to analyze
metrics = ["Accuracy", "Precision", "Recall", "F1_Score"]

# Generate summary report with mean, median, and standard deviation
print("\n----- SUMMARY REPORT -----")

for metric in metrics:
    print("\n-----", metric, "-----")
    print("Mean:", dataframe[metric].mean())
    print("Median:", dataframe[metric].median())
    print("Std Dev:", dataframe[metric].std())

# Show bar charts for each performance metric
for metric in metrics:
    plt.figure()
    plt.bar(dataframe["Model"], dataframe[metric])
    plt.title(f"{metric} Comparison")
    plt.xlabel("Models")
    plt.ylabel(metric)
    
# Display all charts
plt.show()
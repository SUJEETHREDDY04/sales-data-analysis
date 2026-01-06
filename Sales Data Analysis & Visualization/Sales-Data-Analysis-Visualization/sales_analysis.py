import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("sales_data.csv")

# Basic analysis
total_sales = np.sum(data["Sales"])
average_sales = np.mean(data["Sales"])
best_month = data.loc[data["Sales"].idxmax()]
worst_month = data.loc[data["Sales"].idxmin()]

print("Total Sales:", total_sales)
print("Average Monthly Sales:", average_sales)
print("\nBest Month:\n", best_month)
print("\nWorst Month:\n", worst_month)

# Line plot: Monthly Sales Trend
plt.figure()
plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Bar chart: Sales per Month
plt.figure()
plt.bar(data["Month"], data["Sales"])
plt.title("Monthly Sales Distribution")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Scatter plot: Advertising vs Sales
plt.figure()
plt.scatter(data["Advertising_Spend"], data["Sales"], s=200)
plt.title("Advertising Spend vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")
plt.show()

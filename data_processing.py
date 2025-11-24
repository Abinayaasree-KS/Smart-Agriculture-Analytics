# -------------------------------------
# Data Processing for Crop Yield Dataset
# -------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("crop_yield.csv")

print("First 5 Rows:\n", df.head())

# -----------------------------
# 2. Data Cleaning
# -----------------------------

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill or drop missing values based on your dataset
df = df.fillna(df.mean(numeric_only=True))   # fills numeric missing values
df = df.dropna()                             # removes rows with leftover missing values

# Remove duplicates
df.drop_duplicates(inplace=True)

# -----------------------------
# 3. Basic Data Transformation
# -----------------------------

# Convert date column (if exists)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# Example: create new feature (optional)
if "rainfall" in df.columns and "temperature" in df.columns:
    df["weather_score"] = (df["rainfall"] * 0.6) + (df["temperature"] * 0.4)

# -----------------------------
# 4. Statistical Summary
# -----------------------------
print("\nSummary Statistics:\n", df.describe())

# -----------------------------
# 5. Visualizations
# -----------------------------

# Yield distribution
plt.figure(figsize=(6,4))
plt.hist(df["yield"], bins=10)
plt.title("Crop Yield Distribution")
plt.xlabel("Yield")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# If crop type exists, visualize average yield per crop
if "crop_type" in df.columns:
    plt.figure(figsize=(7,4))
    df.groupby("crop_type")["yield"].mean().plot(kind="bar")
    plt.title("Average Yield per Crop Type")
    plt.xlabel("Crop Type")
    plt.ylabel("Average Yield")
    plt.tight_layout()
    plt.show()

# -----------------------------
# 6. Save Processed Dataset
# -----------------------------
df.to_csv("processed_crop_yield.csv", index=False)

print("\nProcessed dataset saved successfully!")

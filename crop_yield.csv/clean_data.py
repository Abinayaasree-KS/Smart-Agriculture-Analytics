import pandas as pd

# STEP 1: Load your dataset
df = pd.read_csv("crop_yield.csv")  # Replace with your actual filename

print("🔹 Original shape:", df.shape)

# STEP 2: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("✅ Columns cleaned:", df.columns.tolist())

# STEP 3: Remove duplicates
df = df.drop_duplicates()

# STEP 4: Strip and format text columns
for col in ['crop', 'season', 'state']:
    df[col] = df[col].astype(str).str.strip().str.title()

# STEP 5: Handle missing values
print("\n🔍 Missing values before:\n", df.isnull().sum())

# Fill numeric columns with mean (if any missing)
numeric_cols = ['area', 'production', 'annual_rainfall', 'fertilizer', 'pesticide', 'yield']
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mean())

# Drop rows with missing crop, year, season
df = df.dropna(subset=['crop', 'crop_year', 'season'])

print("\n✅ Missing values after:\n", df.isnull().sum())

# STEP 6: Convert data types
df['crop_year'] = pd.to_numeric(df['crop_year'], errors='coerce').astype('Int64')
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# STEP 7: Remove outliers (e.g. extremely high yield)
for col in numeric_cols:
    upper_limit = df[col].quantile(0.99)
    df = df[df[col] <= upper_limit]

# STEP 8: Save the cleaned data
df.to_csv("cleaned_agri_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_agri_data.csv'")

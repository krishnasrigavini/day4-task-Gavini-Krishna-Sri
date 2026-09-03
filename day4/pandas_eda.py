import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Ravi', 'Anu', None, 'Sita', 'John'],
    'Age': [25, None, 30, 22, 28],
    'Salary': [50000, 60000, 55000, None, 70000],
    'Dept': ['IT', 'HR', 'IT', 'HR', 'IT']
}

df = pd.DataFrame(data)

print("--- 1. BEFORE Cleaning ---")
print(df)
print("\nMissing values:\n", df.isnull().sum())

# Cleaning
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\n--- 2. AFTER Cleaning ---")
print(df)

# EDA
print("\n--- 3. EDA - Describe ---")
print(df.describe())

print("\n--- 4. Groupby Dept - Avg Salary ---")
print(df.groupby('Dept')['Salary'].mean())

print("\n--- 5. Filter - Age > 25 ---")
print(df[df['Age'] > 25])
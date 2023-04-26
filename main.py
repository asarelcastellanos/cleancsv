import pandas as pd

# Read the CSV file
path = input("Path to CSV File: ")
df = pd.read_csv(path)

# Fill empty cells with data of the cell above it
df[['Department', 'Discipline', 'Course']] = df[['Department', 'Discipline', 'Course']].fillna(method='ffill')

# Replace any remaining empty cells with 0
df = df.fillna(0)

# Write the updated dataframe to a new CSV file
df.to_csv('updated.csv', index=False)

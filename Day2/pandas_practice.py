
import pandas as pd

#  Load the dataset
df = pd.read_csv("Titanic.csv")


# Display first and last five rows
print("First Five Rows:")
print(df.head())

print("Last Five Rows:")
print(df.tail())


# Display dataset information
print("Dataset Information:")
df.info()


# Find missing values
print("Missing Values:")
print(df.isnull().sum())


# Filter data based on a condition
print("Filtered Data:")
print(df[df["Age"] > 40])


# Calculate summary statistics
print("Summary Statistics:")
print(df.describe())

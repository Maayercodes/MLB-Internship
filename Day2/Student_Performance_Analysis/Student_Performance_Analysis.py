
import pandas as pd

# Load the dataset

df = pd.read_csv("StudentsPerformance.csv")

print("Dataset Loaded Successfully!")


# Display Basic Information

print("\nDataset Information:")
print(df.head())

df.info()


# Calculate Average Marks for Each Subject

print("\nAverage Marks of Each Subject:")

print("Math Average:", df["math score"].mean())
print("Reading Average:", df["reading score"].mean())
print("Writing Average:", df["writing score"].mean())


# Identify Top 5 Performing Students

df["average score"] = df[
    ["math score", "reading score", "writing score"]
].mean(axis=1)

top_students = df.sort_values(
    by="average score", ascending=False
).head(5)

print("\nTop 5 Performing Students:")
print(top_students)


# Find Students Scoring Below the Average

average_marks = df["average score"].mean()

below_average = df[df["average score"] < average_marks]

print("\nStudents Scoring Below Average:")
print(below_average)


# Display Total Number of Students

print("\nTotal Number of Students:", len(df))


# Save Analyzed Dataset as a New CSV File

df.to_csv("Analyzed_Students.csv", index=False)

print("\nAnalyzed Dataset Saved Successfully!")

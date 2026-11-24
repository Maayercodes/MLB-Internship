
# Day 2 - Python Practice and Data Analysis

## 1. File Handling and JSON

In this task, I learned how to work with files in Python.

I practiced:
- Creating and opening text files.
- Writing data into files.
- Reading data from files.
- Appending new data to existing files.
- Counting lines in a file.

I also learned how to use JSON in Python. I practiced storing student information in JSON files, reading existing data, updating student records, and adding new records.

Some important functions I learned:
- `open()` - Opens a file.
- `read()` - Reads file content.
- `write()` - Writes data into a file.
- `json.dump()` - Saves Python data into a JSON file.
- `json.load()` - Loads data from a JSON file.

## 2. NumPy

I learned the basics of NumPy and how to work with arrays.

I practiced:
- Creating 1D and 2D arrays.
- Performing arithmetic operations such as addition, subtraction, multiplication, and division.
- Finding maximum and minimum values.
- Calculating mean and sum.
- Reshaping arrays into different dimensions.
- Accessing and slicing array elements.

NumPy makes it easier to perform mathematical operations on arrays.

## 3. Pandas Practice (Titanic Dataset)

For Pandas practice, I used the Titanic dataset.

I learned how to work with CSV datasets using Pandas.

I practiced:
- Loading the Titanic dataset using `read_csv()`.
- Displaying the first five and last five rows.
- Checking dataset information using `info()`.
- Finding missing values using `isnull().sum()`.
- Filtering data based on conditions.
- Calculating summary statistics using `describe()`.

This practice helped me understand how to explore, filter, and analyze real-world datasets using Pandas.

## 4. How File Handling and JSON Work Together

File Handling and JSON can be used together to store and manage data permanently.

In my Student Record Management System, I used JSON to save student records in a file.

When the program starts, it loads existing records from the JSON file. When a new student is added, updated, or deleted, the changes are saved back into the file.

This allows student records to remain available even after closing the program.

## 5. Student Performance Analysis Project

For this project, I used the Students Performance dataset, which contains 1000 student records.

The dataset includes student information such as gender, parental level of education, lunch type, test preparation course, and scores in three subjects:
- Math
- Reading
- Writing

I performed the following analysis:
- Calculated average marks in each subject.
- Identified the top 5 performing students based on their average scores.
- Found students whose average scores were below the overall average.
- Calculated the total number of students.
- Saved the analyzed dataset as a new CSV file.

Through this analysis, I learned how to calculate averages, compare student performance, identify top-performing students, and work with real-world educational data.

## 6. Challenges Faced During Implementation

During these tasks, I faced some challenges:

- Understanding how to read and write data in files.
- Working with JSON data and understanding lists and dictionaries.
- Updating existing student records in a JSON file.
- Handling errors when a file does not exist.
- Understanding NumPy array operations and reshaping.
- Working with Pandas column names and filtering conditions.
- Calculating student averages and sorting records correctly.

## 7. Solutions Implemented

I solved these challenges by practicing each concept step by step.

- Used `try-except` to handle file-related errors and invalid inputs.
- Used `json.load()` and `json.dump()` to read and save student records.
- Used lists and dictionaries to manage student information.
- Used NumPy functions for array calculations.
- Used Pandas functions to load, filter, and analyze CSV data.
- Used loops and conditions to manage student records.
- Tested the programs with different inputs to check their results.

## Conclusion

Day 2 helped me improve my Python programming skills. I learned File Handling, JSON, NumPy, and Pandas. I also developed a persistent Student Record Management System and completed a Student Performance Analysis project using a real dataset.

These tasks improved my understanding of storing data, handling files, working with arrays, and analyzing datasets using Python.


import numpy as np

# Create 1D and 2D Arrays

arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:")
print(arr1)

print("2D Array:")
print(arr2)


# Perform Arithmetic Operations on Arrays

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Find Maximum, Minimum, Mean and Sum

numbers = np.array([10, 20, 30, 40, 50])

print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Mean:", np.mean(numbers))
print("Sum:", np.sum(numbers))


# Reshape Arrays into Different Dimensions

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2, 3)

print("Original Array:")
print(arr)

print("Reshaped Array:")
print(reshaped)


# Slice and Index Arrays

numbers = np.array([10, 20, 30, 40, 50])

print("First Element:", numbers[0])
print("Third Element:", numbers[2])

print("Sliced Array:", numbers[1:4])

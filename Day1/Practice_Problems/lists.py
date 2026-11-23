
# Day 1 - List Practice Problems

# Task 1: Find the largest number in a list

numbers = [10, 45, 23, 89, 12, 67]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)


# Task 2: Find the second largest number
numbers = [10, 45, 23, 89, 12, 67]
largest = numbers[0]
second_largest = None
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num
print(second_largest)

# Task 3: Remove duplicate values

numbers = [10, 20, 30, 20, 40, 10, 50]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)


# Task 4: Reverse a list without using reverse()

numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print(reversed_list)

# Task 5: Find common elements between two lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for num in list1:
    if num in list2:
        common += [num]
print(common)
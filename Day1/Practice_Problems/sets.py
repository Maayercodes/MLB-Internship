
# Day 1 - Set Practice Problems

# Task 1: Find unique values from a list

numbers = [10, 20, 20, 30, 40, 40, 50, 50]
unique_numbers = set()
for num in numbers:
    unique_numbers.add(num)
print(unique_numbers)

# Task 2: Union operation

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
union_set = set1|set2
print(union_set)

# Task 3: Intersection operation
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
intersection_set = set1&set2
print(intersection_set)



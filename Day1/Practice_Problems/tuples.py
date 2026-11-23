
# Day 1 - Tuple Practice Problems

# Task 1: Count occurrences of an element

numbers = (10, 20, 30, 20, 40, 20, 50)
count =0
for num in numbers:
    if num == 20:
        count += 1
print(count)

# Task 2: Convert tuple into list

my_tuple = (10, 20, 30, 40, 50)
my_list = []
for num in my_tuple:
    my_list += [num]
print(my_list)

# Task 3: Convert list into tuple

my_list = [100, 200, 300, 400, 500]
my_tuple = ()
for num in my_list:
    my_tuple += (num,)
print(my_tuple)
# Create a text file and write data into it.
file = open("data.txt", "w")
file.write("My name is Maayer.\n")
file.write("I am learning python.\n")
file.close()

# Read and display file contents.
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Append new data to an existing file.
file = open("data.txt", "a")
file.write("I am enjoying the learning process.\n")
file.close()

# Count the number of lines in a file.
file = open("data.txt", "r")
count = 0
for line in file:
    count = count + 1
print(count)
file.close()
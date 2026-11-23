
# Day 1 - Dictionary Practice Problems

# Task 1: Create a student record dictionary
student = {
    "name": "Maayer",
    "roll no" : 99,
    "age" : 21,
    "department" : "AI",
    "marks" : 85
}
print(student)
# Task 2: Calculate average marks of students

students = {
    "Ali": 85,
    "Ahmed": 75,
    "Maayer": 90,
    "Hassan": 80
}
total = 0
count = 0
for marks in students.values():
    total += marks
    count += 1
average = total / count
print(average)
# Task 3: Count frequency of words in a sentence

sentence = "python is easy and python is powerful"
words = []
word = ""
for char in sentence:
    if char != " ":
        word += char
    else:
        words += [word]
        word = ""

words += [word]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
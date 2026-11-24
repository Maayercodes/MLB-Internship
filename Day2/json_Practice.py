# Store student information in a JSON file.
import json

student = [
    {
        "name": "Maayer Hassan",
        "age": 21,
        "grade": "A",
        "course": "Artificial Intelligence"
    }
]
file = open("student.json", "w")
json.dump(student, file, indent=4)
file.close()

# Read data from a JSON file.
import json

file = open("student.json", "r")
student = json.load(file)
print(student)
file.close()

# Update an existing student's information.
import json

file = open("student.json", "r")
student = json.load(file)
file.close()

student[0]["age"] = 22
student[0]["grade"] = "A+"

file = open("student.json", "w")
json.dump(student, file, indent=4)
file.close()

print("Student information updated successfully!")

# Add a new student to the JSON file.
import json

file = open("student.json", "r")
students = json.load(file)
file.close()

new_student = {
    "name": "Minhaj",
    "age": 21,
    "grade": "B",
    "course": "Data Science"
}

students.append(new_student)

file = open("student.json", "w")
json.dump(students, file, indent=4)
file.close()

print("New student added successfully!")
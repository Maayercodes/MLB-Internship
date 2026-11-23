
# Student Grading System

student_name = input("Enter student name: ")
student_class = input("Enter student class: ")

subjects = []
marks_list = []

total_subjects = int(input("Enter number of subjects: "))

for i in range(total_subjects):

    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))

    subjects += [subject]
    marks_list += [marks]
#Calculate total marks
total_marks = 0
for marks in marks_list:
    total_marks += marks

#Calculate average marks
average_marks = total_marks / total_subjects

#Assign grade
if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
else:
    grade = "F"

#Display student report

print("\n--------- STUDENT REPORT --------")

print("Name:", student_name)
print("Class:", student_class)

# Display individual subject marks
for i in range(total_subjects):
    print(subjects[i] + ":", marks_list[i])
# Display total marks
print("Total Marks:", total_marks)
# Display average
print("Average Marks:", average_marks)
# Display grade
print("Grade:", grade)

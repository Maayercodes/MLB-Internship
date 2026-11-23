# version 1 (Student Record Management System)
students = []

while True:
    print("------ STUDENT RECORD MANAGEMENT SYSTEM ------")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":

        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        if name == "" or roll_no == "" or age == "" or course == "":
            print("All fields are required!")

        else:
            found = False

            for student in students:
                if student["roll_no"] == roll_no:
                    found = True

            if found:
                print("Roll number already exists!")

            else:
                student = {
                    "name": name,
                    "roll_no": roll_no,
                    "age": age,
                    "course": course
                }

                students += [student]

                print("Student added successfully!")

    # 2. View All Students
    elif choice == "2":

        if students == []:
            print("No student records found!")

        else:
            for student in students:
                print("\n----------------------")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Age:", student["age"])
                print("Course:", student["course"])

    # 3. Search Student
    elif choice == "3":

        search_roll = input("Enter roll number: ")

        found = False

        for student in students:
            if student["roll_no"] == search_roll:

                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Age:", student["age"])
                print("Course:", student["course"])

                found = True

        if not found:
            print("Student not found!")

    # 4. Update Student
    elif choice == "4":

        update_roll = input("Enter roll number: ")

        found = False

        for student in students:
            if student["roll_no"] == update_roll:

                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Course")

                update_choice = input("Choose field: ")

                if update_choice == "1":
                    student["name"] = input("Enter new name: ")
                    print("Name updated successfully!")

                elif update_choice == "2":
                    student["age"] = input("Enter new age: ")
                    print("Age updated successfully!")

                elif update_choice == "3":
                    student["course"] = input("Enter new course: ")
                    print("Course updated successfully!")

                else:
                    print("Invalid choice!")

                found = True

        if not found:
            print("Student not found!")

    # 5. Delete Student
    elif choice == "5":

        delete_roll = input("Enter roll number: ")

        found = False
        updated_students = []

        for student in students:

            if student["roll_no"] == delete_roll:
                found = True

            else:
                updated_students += [student]

        if found:
            students = updated_students
            print("Student deleted successfully!")

        else:
            print("Student not found!")

    # 6. Total Students
    elif choice == "6":

        count = 0

        for student in students:
            count += 1

        print("Total Students:", count)

    # 7. Exit
    elif choice == "7":

        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please try again.")

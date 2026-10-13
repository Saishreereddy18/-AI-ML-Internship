print("===== Student Record Management System =====")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll_no = input("Enter roll number: ")
        name = input("Enter student name: ")
        branch = input("Enter branch: ")
        marks = input("Enter marks: ")

        student = {
            "roll_no": roll_no,
            "name": name,
            "branch": branch,
            "marks": marks
        }

        with open("students.txt", "a") as file:
            file.write(
                student["roll_no"] + "," +
                student["name"] + "," +
                student["branch"] + "," +
                student["marks"] + "\n"
            )

        print("Student added successfully!")

    # View Students
    elif choice == "2":
        print("\n===== Student Records =====")

        with open("students.txt", "r") as file:
            records = file.readlines()

        if len(records) == 0:
            print("No student records found.")
        else:
            for record in records:
                data = record.strip().split(",")

                print("Roll No:", data[0])
                print("Name:", data[1])
                print("Branch:", data[2])
                print("Marks:", data[3])
                print("--------------------")

    # Search Student
    elif choice == "3":
        search_roll = input("Enter roll number to search: ")

        with open("students.txt", "r") as file:
            records = file.readlines()

        found = False

        for record in records:
            data = record.strip().split(",")

            if data[0] == search_roll:
                print("\n===== Student Found =====")
                print("Roll No:", data[0])
                print("Name:", data[1])
                print("Branch:", data[2])
                print("Marks:", data[3])
                found = True

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Thank you for using the system!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
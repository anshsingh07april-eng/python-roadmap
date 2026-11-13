#Q12. Student marks menu. Keep a dictionary that maps a student name to a list of marks. Make a menu: 1. Add student, 2. Add a mark, 3. Show a student's average, 4. Show the topper, 5. Exit. Handle unknown names and marks outside 0 to 100.
students = {}

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Add a mark")
    print("3. Show a student's average")
    print("4. Show the topper")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name not in students:
            students[name] = []
        else:
            print("Student already exists.")

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            try:
                mark = float(input("Enter mark (0-100): "))
                if 0 <= mark <= 100:
                    students[name].append(mark)
                else:
                    print("Invalid mark. Please enter a mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students and students[name]:
            average = sum(students[name]) / len(students[name])
            print(f"Average mark for {name}: {average:.2f}")
        else:
            print("Student not found or has no marks.")

    elif choice == "4":
        if students:
            topper = max(students, key=lambda n: sum(students[n]) / len(students[n]) if students[n] else 0)
            topper_avg = sum(students[topper]) / len(students[topper])
            print(f"The topper is {topper} with an average of {topper_avg:.2f}")
        else:
            print("No students available.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
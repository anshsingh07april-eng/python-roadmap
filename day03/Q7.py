#Q7. Student database. Use a dictionary that maps a student name to a list of marks. Build a menu-driven program with separate functions: add a student, add a mark, show a student's average, show the topper, and exit. Reject unknown names, marks outside 0 to 100, and non-numeric input. The menu must loop until the user exits.

student_database = {}


# 1. Add a student
def add_student(name):
    if name not in student_database:
        student_database[name] = []
        print(f"Student added: {name}")
    else:
        print("Student already exists.")


# 2. Add marks
def add_mark(name, mark):
    if name not in student_database:
        print("Student not found.")
        return

    if 0 <= mark <= 100:
        student_database[name].append(mark)
        print(f"Mark added for {name}: {mark}")
    else:
        print("Invalid mark. Enter a number between 0 and 100.")


# 3. Show student's average
def show_average(name):
    if name not in student_database:
        print("Student not found.")
        return

    marks = student_database[name]

    if not marks:
        print(f"No marks available for {name}.")
        return

    average = sum(marks) / len(marks)
    print(f"Average for {name}: {average:.2f}")


# 4. Show topper
def show_topper():
    students_with_marks = {
        name: marks
        for name, marks in student_database.items()
        if marks
    }

    if not students_with_marks:
        print("No marks available to find the topper.")
        return

    topper = max(
        students_with_marks,
        key=lambda name: sum(students_with_marks[name]) /
                         len(students_with_marks[name])
    )

    topper_avg = (
        sum(students_with_marks[topper]) /
        len(students_with_marks[topper])
    )

    print(f"Topper: {topper} with average: {topper_avg:.2f}")


# 5. Main menu
def main():
    while True:
        print("\n===== STUDENT DATABASE =====")
        print("1. Add Student")
        print("2. Add Mark")
        print("3. Show Average")
        print("4. Show Topper")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ").strip()

            if name:
                add_student(name)
            else:
                print("Student name cannot be empty.")

        elif choice == "2":
            name = input("Enter student name: ").strip()

            try:
                mark = float(input("Enter mark (0-100): "))
                add_mark(name, mark)

            except ValueError:
                print("Invalid input. Please enter a numeric mark.")

        elif choice == "3":
            name = input("Enter student name: ").strip()
            show_average(name)

        elif choice == "4":
            show_topper()

        elif choice == "5":
            print("Exiting Student Database. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Program execution
if __name__ == "__main__":
    main()

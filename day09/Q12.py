#Q12. Student database in OOP. Rebuild your Day 3 student database (name, marks, average, topper) using classes Student and School.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(f"{student.name}: {student.average():.2f}")
school = School()
while True:
    action = input("Choose an action (add, show, exit): ").lower()
    if action == "add":
        name = input("Enter student name: ")
        marks_input = input("Enter marks separated by spaces: ")
        marks = list(map(float, marks_input.split()))
        student = Student(name, marks)
        school.add_student(student)
        print(f"Student added: {name}")
    elif action == "show":
        print("Students and their averages:")
        school.show_students()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please choose 'add', 'show', or 'exit'.")
#Q9. Compare and sort. Add __eq__ and __lt__ to a Student class so that two students can be compared by their average mark. Create 4 students and print them sorted from best to worst with sorted(students, reverse=True).
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average() == other.average()
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average() < other.average()
        return False

students = [
    Student("Alice", [85, 90, 78]),
    Student("Bob", [92, 88, 95]),
    Student("Charlie", [76, 82, 89]),
    Student("Diana", [95, 91, 87])
]

sorted_students = sorted(students, reverse=True)
for student in sorted_students:
    print(f"{student.name}: {student.average():.2f}")
print("Students have been sorted by average marks!")
print("Best to worst students:")
for student in sorted_students:
    print(f"{student.name}: {student.average():.2f}")
print("All students have been displayed!")
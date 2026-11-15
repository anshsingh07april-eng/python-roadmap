#Q3. Employee. Write an Employee class with name and salary, a method give_raise(percent) that increases the salary, and __str__ so that print(emp) shows something like Riya: Rs. 55000.0. Check that a negative raise is rejected with a friendly message.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        if percent < 0:
            print("Friendly message: Negative raise is not allowed.")
        else:
            self.salary += self.salary * percent / 100

    def __str__(self):
        return f"{self.name}: Rs. {self.salary:.1f}"

emp = Employee("Riya", 50000)
print(emp)
emp.give_raise(10)
print(emp)
emp.give_raise(-5)
print(emp)
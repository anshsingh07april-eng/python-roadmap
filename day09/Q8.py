#Q8. Manager. Write an Employee class (name, salary). Write Manager that inherits from Employee, adds a list team, and has methods add_member(employee) and show_team(). Use super().__init__(...) in the child class.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.team = []

    def add_member(self, employee):
        self.team.append(employee)

    def show_team(self):
        for member in self.team:
            print(f"- {member.name} (${member.salary})")
print("Manager and Team Members:")
manager = Manager("Alice", 90000)
while True:
    name = input("Enter team member's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    salary = float(input(f"Enter {name}'s salary: "))
    employee = Employee(name, salary)
    manager.add_member(employee)

manager.show_team()
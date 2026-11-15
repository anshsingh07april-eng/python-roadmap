#Q10. Counting objects. Add a class variable count = 0 to a class Visitor. Increase it inside __init__ so that it tells how many visitors have been created. Create 4 visitors and print Visitor.count. In a comment, explain the difference between a class variable and an instance variable.
class Visitor:
    count = 0

    def __init__(self, name):
        self.name = name
        Visitor.count += 1

visitor1 = Visitor("Alice")
visitor2 = Visitor("Bob")
visitor3 = Visitor("Charlie")
visitor4 = Visitor("Diana")

print(f"Number of visitors created: {Visitor.count}")
print("All visitors have been created!")
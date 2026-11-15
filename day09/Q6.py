#Q6. Animals. Write a parent class Animal with name and a method speak() that returns "...". Write Dog and Cat that inherit from it and override speak(). Put one of each in a list and loop over the list, printing what each says.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
print("All animals have spoken!")
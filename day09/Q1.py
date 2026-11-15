#Q1. Car. Write a Car class with brand and speed (starts at 0). Add accelerate(amount), brake(amount) (the speed must never go below 0) and show(). Create one car and call each method at least twice.
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def show(self):
        print(f"Car: {self.brand}, Speed: {self.speed}")

my_car = Car("Toyota")
my_car.show()
my_car.accelerate(20)
my_car.show()
my_car.brake(10)
my_car.show()
my_car.accelerate(30)
my_car.show()
print("Final speed:", my_car.speed)
if my_car.speed < 0:
    print("Speed is below 0, which should not happen.")
else:
    print("Speed is valid.")
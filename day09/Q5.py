#Q5. Shopping cart. Write a ShoppingCart class that stores items in a list of dictionaries. Add add_item(name, price, qty=1), total() and show() that prints each item and the total. Add 3 items and print the bill.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def total(self):
        return sum(item["price"] * item["qty"] for item in self.items)

    def show(self):
        for item in self.items:
            print(f"{item['name']}: ${item['price']:.2f} x {item['qty']} = ${item['price'] * item['qty']:.2f}")
        print(f"Total: ${self.total():.2f}")

cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Banana", 0.75, 2)
cart.add_item("Orange", 2.00, 1)
cart.show()
print(f"Total amount to pay: ${cart.total():.2f}")
print("Thank you for shopping with us!")
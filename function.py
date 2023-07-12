class Warehouse:
    def __init__(self):
        self.item = {}
        self.log = []
        self.balance = 0

    def review(self):
        starting_index = int(input("Enter the starting index: "))
        ending_index = int(input("Enter the ending index: "))
        for log in self.log[starting_index:ending_index]:
            log.print()


class Purchase:
    def __init__(self):
        self.item = ""
        self.price = 0
        self.quantity = 0

    def current(self):
        self.item = input("Enter the item name: ")
        self.price = input("Enter the item price: ")
        self.quantity = input("Enter the item quantity purchased: ")

    def execute(self, warehouse):
        if warehouse.balance < self.price * self.quantity:
            print("Insufficient funds")
            return
        warehouse.balance -= self.price * self.quantity
        if self.item not in warehouse.items:
            warehouse.items[self.item] = 0
            warehouse.items[self.item] += self.quantity
            warehouse.log.append(self)

    def print(self):
        print(f"Purchased {self.item} for {self.quantity} in ${self.price} per item")


class Sales:
    def __init__(self):
        self.item = ""
        self.price = 0
        self.quantity = 0

    def current(self):
        self.item = input("Enter the item name: ")
        self.price = input("Enter the item price: ")
        self.quantity = input("Enter the item quantity sold: ")

    def execute(self, warehouse):
        if warehouse.quantity < self.quantity:
            print("Insufficient stock")
            return
        warehouse.quantity -= self.quantity
        if self.item not in warehouse.items:
            print("Item not found")
        warehouse.items[self.item] -= self.quantity
        warehouse.log.append(self)

    def print(self):
        print(f"Sold {self.item} for {self.quantity} in ${self.price} per item")


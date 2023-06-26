account = 0
warehouse = {"cup": 30, "spoon": 10}
log = []

while True:
    available_commands = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]
    command = input("Enter the command: balance/ sale/ purchase/ account/ list/ warehouse/ review/ end")
    print("Enter the command: balance/ sale/ purchase/ account/ list/ warehouse/ review/ end")
    if command not in available_commands:
        print("Error, please input valid command")

    if command == "end":
        break

    if command == "account":
        print("Current account value", account)

    if command == "balance":
        balance = float(input("Enter the amount to add/subtract"))
        if - balance > account:
            print("Insufficient funds")
            continue
        account += balance
        log.append(f"{balance}")

    if command == "sale":
        product_name = input("Enter the product name")
        if product_name not in warehouse:
            print("Product not found")
            continue
        quantity = int(input("Enter the quantity sold"))
        if quantity > warehouse[product_name]:
            print("Insufficient stock")
            continue
        price = float(input("Enter the product price"))
        sale = price * quantity
        print("\nSales proceed")
        print("\nTotal sales:", sale)
        account += sale
        warehouse[product_name] -= quantity
        log.append(f"{sale}")

    if command == "purchase":
        product_name = input("Enter the product name")
        if product_name not in warehouse:
            print("Product not found")
            continue
        quantity = int(input("Enter the quantity purchased"))
        price = float(input("Enter the purchase price per item"))
        purchase = price * quantity
        account -= purchase
        if price * quantity > account:
            print("insufficient funds, order cancelled")
            continue
        print("\nPurchase completed")
        print("\nTotal purchase", purchase)
        warehouse[product_name] += quantity
        log.append(f"{purchase}")

print("Current account balance", account)
print("Total inventory in warehouse", warehouse)

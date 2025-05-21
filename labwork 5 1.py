def print_receipt(items):
    print("----------------------------------")
    print("| Item       | Qty  | Price  | Total  |")
    print("----------------------------------")
    total_amount = 0
    for item, qty, price in items:
        total = qty * price
        total_amount += total
        print(f"| {item:<10} | {qty:^4} | {price:<5}$ | {total:<5}$ |")
    print("----------------------------------")
    print(f"Total: {total_amount}$")

items = [("Laptop", 1, 1000), ("Phone", 2, 700), ("Keyboard", 3, 50)]
print_receipt(items)

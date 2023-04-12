def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        discount = total * 0.1
        total -= discount
    return total

quantity = float(input("Enter quantity: "))
price = float(input("Enter price: "))

total = compute_total(quantity, price)

print("Quantity:", quantity)
print("Price:", price)
print("Total:", total)
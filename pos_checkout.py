import sys

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

items = []
subtotal = 0.0
total_units = 0

while True:
    name_input = input("Item name (or DONE to finish): ").strip()
    if name_input.upper() == "DONE":
        break
    if not name_input:
        print("Item name cannot be empty. Please try again.")
        continue

    while True:
        try:
            price = float(input(f"Unit price for '{name_input}': "))
            if price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            qty = int(input(f"Quantity for '{name_input}': "))
            if qty < 1:
                print("Quantity must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    subtotal += price * qty
    total_units += qty
    items.append((name_input, price, qty))

if total_units >= 10 or subtotal >= 100:
    discount_pct = 10
else:
    discount_pct = 0

discount_amount = subtotal * (discount_pct / 100)
total = subtotal - discount_amount

perk_applied = seed % 2 != 0
if perk_applied:
    total = max(0.0, total - 3.00)

print()
print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_pct}%")
print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
print(f"Total: ${total:.2f}")

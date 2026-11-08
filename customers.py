# Exercise 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 1250.00
}

print("Exercise 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Multiple Customers

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: Safe Lookup

print("\nExercise 3")

print(customer.get("email", "Email not found"))

try: 
    print(customer["email"])
except KeyError:
    print("Email not found")

# Exercise 4: Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer.keys():
        print(key)

# Exercise 5: Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Customer Tier: {customer['tier']}")
print(f"Purchase Price: ${purchase_price:.2f}")
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")
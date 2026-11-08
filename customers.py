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

customer["tier"] = "Platinum"
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
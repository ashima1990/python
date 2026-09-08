#================================================================
# FARM HARVEST calculator
#================================================================

# --- Assignment Operator (=) ---

# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

 # --- Arithmetic Operators (+, -, *, /) ---

# Calculate total and average harvest

total   = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest      :", total, "kg")
print("Average harvest    :", average, "kg")

# Price per kg is 15 rupees — calculate total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings     : Rs.", earnings)

# Floor division and modulus

floor_division = total // 5
modulus = total % 5
print("Full bags packed   :", floor_division)
print("Leftover grain     :", modulus, "kg")

# --- Comparison Operators (>, <, ==, >=) ---

# Compare this year's harvest with last year

last_year = 500
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

# --- Assignment Operators (+=, -=) ---

# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop   :", total, "kg")

# Subtract 15 kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")
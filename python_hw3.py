
print("Welcome to the Power Calculator!")


# Step 1: Get the base number from the user
base = float(input("Enter the base number: "))

# Step 2: Get the exponent from the user
exponent = int(input("Enter the exponent: "))

# Step 3: Calculate the power using a loop
result = 1
for i in range(1, exponent + 1):
    if i <= exponent:
     result = result * base
     print(result)
    else:
        print("Wrong input")
print(f"step{i}: {base} raised to the power of {i} is: {result}")


# Step 4: Print the result
print(f"The result of {base} raised to the power of {exponent} is: {result}")

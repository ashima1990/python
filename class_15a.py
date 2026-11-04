# using try ang except
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
except ValueError:
    print("Invalid .")
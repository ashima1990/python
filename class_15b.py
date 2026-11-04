try:
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    result=num1/num2
    print("result is:",result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("this will execute no matter what")

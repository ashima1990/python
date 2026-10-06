#===================== guessing game =====================#
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 attempts to guess the number.")
# TAKING A RANDOM NUMBER BETWEEN 1 AND 100
number = 42  # I am using a fixed number.

# Counting the number of guesses
a=1
b=5
print("#============= note=================" \
+"Very Cold means near, Cold means close, Hot means very close, and Very Hot means extremely close to the number. =============#")
print("Type your first guess:")
guess = int(input())

while a < b+1:
    if guess == number:
        print("Congratulations! You guessed the number correctly.")    
    elif guess < number and guess >= number - 12:
        print("Your guess is very hot.")
        print("Try again:")
        guess = int(input())
    elif guess<number and guess <number - 13:
        print("Your guess is hot.")
        print("Try again:")
        guess = int(input())
    elif guess < number and guess <= number -23:
        print("Your guess is cold.")
        print("Try again:")
        guess = int(input())
    elif guess < number and guess <= number - 33:
        print("Your guess is very cold.")
        print("Try again:")
        guess = int(input())
    else: 
        print("Your guess is too high.")
        print("Try again:")
        guess = int(input())
        break

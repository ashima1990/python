import random # importing random module
playing = True #initialise
number = str(random.randint(0,9)) #random in-built function

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the condition is true    
while playing:
    guess = input("Enter your guess: ") #take input from user
    if guess == number: #check the condition
        print("Congratulations! You guessed the number correctly.")
        print("The number was: " + number)
        break

    else:
        print("Sorry, that's not the correct number. Try again!")
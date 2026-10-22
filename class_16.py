import random # importing the random module


while True: # iterate loop
    user_input= input("Enter achoice (rock/paper/scissors): ") # take input from user
    possible_choices= ["rock", "paper", "scissors"] # list of choices
    computer_choice= random.choice(possible_choices)
    print(f"Computer chose: {computer_choice}, you chose: {user_input}")
    #display both choices what is selected by you and your computer

    #conditions to check you won the game 
    if user_input == computer_choice: 
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
#take input for playing again
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
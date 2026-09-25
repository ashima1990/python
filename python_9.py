# My Chore Checklist Countdown
 # Part 1: Set todays total number of chores
total_chores = 6
original_count = total_chores
print(f"Today you have {total_chores} chores to do.")
print("Let's get started!\n")
print("Chore Checklist:")
chore = input("Name of chores here: ")
chores = [chore]

# PART 2: Keep a counter for completed chores and the current chore number
completed_count = 0
chores = []
while completed_count < original_count:

    # PART 4: Work out the current chore's name from its number
    if completed_count == 1: next_chore = chores[1]
    elif completed_count == 2: next_chore = chores[2]
    elif completed_count == 3: next_chore = chores[3]
    elif completed_count == 4: next_chore = chores[4]
    elif completed_count == 5: next_chore = chores[5]
    else: next_chore = chores[0]

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")


    # PART 5: If the user has completed the chore, increment the completed count and chore number
    if answer=="yes":
        completed_count += 1
        chore_num += 1
        print(f"Great job! You have completed {completed_count} out of {original_count} chores.\n")
    else:
        print("Okay, finish it and check again!")

    # PART 6: Print how many chores remain after each check
    print("Chores remaining:", total_chores - completed_count)
    print()

    # PART 7: If the user has completed all chores, print a congratulatory message
    if completed_count == original_count:
        print("Congratulations! You have completed all your chores for today!")
    else:
        print("You still have to complete your chores. Keep going!")


    # PART 8: A safe look at what an infinite loop would look like
print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("Test value is less than or equal to 0, so this loop will run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

    # PART 9: Print the final chore checklist summary
print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores Assigned Today:", original_count)
print("Chores Completed:", completed_count)
print("Chores Remaining:", total_chores - completed_count)
print("======================================")
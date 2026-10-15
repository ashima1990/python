# parking ticket helper

def ticket(hrs,rate):
    total = 0
    total+= hrs * rate
    return total
rate = 45

print("========== PARKING TICKET HELPER ==========")
hrs = float(input("Enter the number of hours you are staying here: "))
total = ticket(hrs, rate)
print(f"The total cost of your parking is: ${total:.2f}")

print("Accepted coins are: 25, 10, 05, or 01\n")
coins_inserted = 0
coins_total = 0

while True:
    coin = int(input("Insert a coin (25, 10, 05, or 01): "))

    if coin != 25 and coin != 10 and coin != 5 and coin != 1:
        print("Invalid coin, try again!\n")
        continue

    coins_total += coin
    coins_inserted += 1
    print(f"Inserted {coin}, Total coins inserted: {coins_inserted}.\n")

    if coins_total >= total:
        print ("enough money inserted.\n")
        break


change_due = coins_total - total
print(f"Change due: ${change_due:.2f}")

print("\n===== PARKING SUMMARY =====")
print(f"Hours parked: {hrs}")
print(f"Rate per hour: ${rate}")
print(f"Total cost: ${total:.2f}")
print(f"Coins inserted: {coins_inserted}")
print(f"Total paid: ${coins_total:.2f}")
print(f"Change given: ${change_due:.2f}")
print("THANKS FOR PARKING HERE!")
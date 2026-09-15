print("========Smart School day Planner========")
print ("Answer my 3 quick questions and I will plan the day for you!")

day      = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather  = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print("")
print(f"Planning your day for {day}.")
print("-"*35)

# Topic 1 - if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last day of the week. Return all the library books!")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    : Regular school day. Focus on your studies.")
else:
    print("Day type    : Day not recognised. Please check the spelling.")

# Topic 2 -- AND operator: sunny AND homework done
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!")

# Topic 3 -- OR operator: rainy OR cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")

# Topic 4 -- NOT operator: homework NOT done
if not (homework == "yes"):
    print(" Finish your homework before going out to play.")

# Topic 5 -- Combining AND + OR + NOT together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan: Stay home and finish your homework then watch your favorite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")


print()
print("========Smart School day Planner Complete!========")
print("HAVE A GREAT DAY!")
print("================================RIDE SELECTOR==================================")
print("Select your ride:")
print("1. Bike")
print("2. Car")
print("3. Bus")
print("4. Train")

print ()
ride = input("Enter the number of your ride choice (1-4): ").strip()

if ride == "1":
    print("Pick your preferred Bike.")
    print("1. Mountain Bike")
    print("2. Motor Bike")
    print("3. Road Bike")
    print()
    bike_choice = input("Enter the number of your bike choice (1-3): ").strip()
    if bike_choice == "1":
        print("You selected Mountain Bike. Enjoy your ride!")
        print("TOP SPEED: 40 km/h")
        print("BEST FOR: off-road trails")

    elif bike_choice == "2":
        print("You selected Motor Bike. Enjoy your ride!")
        print("TOP SPEED: 60 km/h")
        print("BEST FOR: city roads and highways")
        
    else:
         print("You selected Road Bike. Enjoy your ride!")
         print("TOP SPEED: 55 km/h")
         print("BEST FOR: paved roads")


elif ride == "2":
    print("You selected Car. Enjoy your ride!")
    print("The best mode of car for travel.")
    print("1. Sedan")
    print("2. SUV")
    print("3. Sports Car")

    print()
    car_choice = input("Enter the number of your car choice (1-3): ").strip()

    if car_choice == "1":
        print("You selected Sedan. Enjoy your ride!")
        print("TOP SPEED: 120 km/h")
        print("BEST FOR: city driving and long distance travel")

    elif car_choice == "2":
        print("You selected SUV. Enjoy your ride!")
        print("TOP SPEED: 100 km/h")
        print("BEST FOR: off-road adventures and family trips")

    else:
        print("You selected Sports Car. Enjoy your ride!")
        print("TOP SPEED: 200 km/h")
        print("BEST FOR: racing and high-speed driving")

elif ride == "3":
    print("You selected Bus. Enjoy your ride!")
    print("The best mode of bus for travel.")
    print("1. City Bus")
    print("2. Intercity Bus")
    print("3. Double Decker Bus")

    print()
    bus_choice = input("Enter the number of your bus choice (1-3): ").strip()

    if bus_choice == "1":
        print("You selected City Bus. Enjoy your ride!")
        print("TOP SPEED: 60 km/h")
        print("BEST FOR: short distance travel within the city")

    elif bus_choice == "2":
        print("You selected Intercity Bus. Enjoy your ride!")
        print("TOP SPEED: 80 km/h")
        print("BEST FOR: long distance travel between cities")

    else:
        print("You selected Double Decker Bus. Enjoy your ride!")
        print("TOP SPEED: 70 km/h")
        print("BEST FOR: sightseeing and city tours")

elif ride == "4":
    print("You selected Train. Enjoy your ride!")
    print("The best mode of train for travel.")
    print("1. High-Speed Train")
    print("2. Commuter Train")

    print()
    train_choice = input("Enter the number of your train choice (1 or 2): ").strip()

    if train_choice == "1":
        print("You selected High-Speed Train. Enjoy your ride!")
        print("TOP SPEED: 300 km/h")
        print("BEST FOR: long distance travel at high speed")

    else:
        print("You selected Commuter Train. Enjoy your ride!")
        print("TOP SPEED: 100 km/h")
        print("BEST FOR: daily commuting and short distance travel")


else:
    print("Invalid ride choice. Please select a valid option (1-4).")


print()
print("==============================RIDE SELECTOR COMPLETE!==============================")  
print("================================")
print("HAVE A GREAT RIDE!")         
print("ENJOY YOUR JOURNEY!")
print("================================")
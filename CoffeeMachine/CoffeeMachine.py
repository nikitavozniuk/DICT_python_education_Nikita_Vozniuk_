water_for_cup = 200
milk_for_cup = 50
coffee_beans_for_cup = 15

water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))

cups_of_coffee = int(input("Write how many cups of coffee you will need: "))

if water_for_cup * cups_of_coffee < water and milk_for_cup * cups_of_coffee < milk and coffee_beans_for_cup * cups_of_coffee < coffee_beans:
    cup_counter = 0
    if cups_of_coffee * water_for_cup < water and cups_of_coffee * milk_for_cup < milk and cups_of_coffee * coffee_beans_for_cup < coffee_beans:
        water_left = water - (water_for_cup * cups_of_coffee)
        milk_left = milk - (milk_for_cup * cups_of_coffee)
        coffee_beans_left = coffee_beans - (coffee_beans_for_cup * cups_of_coffee)
        while water_left >= water_for_cup and milk_left >= milk_for_cup and coffee_beans_left >= coffee_beans_for_cup:
            cup_counter += 1
            water_left -= water_for_cup
            milk_left -= milk_for_cup
            coffee_beans_left -= coffee_beans_for_cup
    if cup_counter > 0:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(cup_counter))
    else:
        print("Yes, I can make that amount of coffee")
elif water_for_cup * cups_of_coffee > water or milk_for_cup * cups_of_coffee > milk or coffee_beans_for_cup * cups_of_coffee > coffee_beans:
    cup_counter = 1
    while water > water_for_cup * cup_counter:
        water -= water_for_cup * cup_counter
        cup_counter += 1
    print("No, I can make only {} cups of coffee".format(cup_counter))
elif water == 0 or milk == 0 or coffee_beans == 0:
    print("No, I can make only 0 cups of coffee")

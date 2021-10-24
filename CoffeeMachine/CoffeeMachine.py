def CoffeeMachine(water, milk, coffee_beans, cups, money):
    print("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money
    """.format(water, milk, coffee_beans, cups, money))

    action = str(input("Write action (buy, fill, take): "))
    if action == "buy":
        choice_to_buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if choice_to_buy == 1:
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4
        elif choice_to_buy == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
        elif choice_to_buy == 3:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6

        CoffeeMachine(water, milk, coffee_beans, cups, money)
    elif action == "fill":
        water_filling = int(input("Write how many ml of water you want to add: "))
        milk_filling = int(input("Write how many ml of milk you want to add: "))
        coffee_beans_filling = int(input("Write how many grams of coffee beans you want to add: "))
        cups_filling = int(input("Write how many disposable coffee cups you want to add: "))

        water += water_filling
        milk += milk_filling
        coffee_beans += coffee_beans_filling
        cups += cups_filling

        CoffeeMachine(water, milk, coffee_beans, cups, money)
    elif action == "take":
        print("I gave you {}".format(money))

        CoffeeMachine(water, milk, coffee_beans, cups, money=0)


CoffeeMachine(400, 540, 120, 9, 550)

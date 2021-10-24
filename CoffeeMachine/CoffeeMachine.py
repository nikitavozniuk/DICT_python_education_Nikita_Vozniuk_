def CoffeeMachine(water, milk, coffee_beans, cups, money):
    action = str(input("Write action (buy, fill, take, remaining, exit): "))
    if action == "buy":
        choice_to_buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
        if choice_to_buy == 1:
            if water - 250 >= 0:
                water -= 250
            else:
                print("Sorry, not enough water!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if coffee_beans - 16 >= 0:
                coffee_beans -= 16
            else:
                print("Sorry, not enough coffee beans!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if cups - 1 >= 0:
                cups -= 1
            else:
                print("Sorry, not enough cups!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            money += 4
            print("I have enough resources, making you a coffee!")
        elif choice_to_buy == 2:
            if water - 350 >= 0:
                water -= 350
            else:
                print("Sorry, not enough water!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if milk - 75 >= 0:
                milk -= 75
            else:
                print("Sorry, not enough milk!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if coffee_beans - 20 >= 0:
                coffee_beans -= 20
            else:
                print("Sorry, not enough coffee beans!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if cups - 1 >= 0:
                cups -= 1
            else:
                print("Sorry, not enough cups!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            money += 7
            print("I have enough resources, making you a coffee!")
        elif choice_to_buy == 3:
            if water - 200 >= 0:
                water -= 200
            else:
                print("Sorry, not enough water!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if milk - 100 >= 0:
                milk -= 100
            else:
                print("Sorry, not enough milk!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if coffee_beans - 12 >= 0:
                coffee_beans -= 12
            else:
                print("Sorry, not enough coffee beans!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            if cups - 1 >= 0:
                cups -= 1
            else:
                print("Sorry, not enough cups!")
                CoffeeMachine(water, milk, coffee_beans, cups, money)

            money += 6
            print("I have enough resources, making you a coffee!")

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
    elif action == "remaining":
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money
        """.format(water, milk, coffee_beans, cups, money))

        CoffeeMachine(water, milk, coffee_beans, cups, money)
    elif action == "exit":
        return True


CoffeeMachine(400, 540, 120, 9, 550)

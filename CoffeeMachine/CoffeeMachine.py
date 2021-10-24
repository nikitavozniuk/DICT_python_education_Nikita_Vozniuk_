class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money, actions):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.actions = actions

    def Action(self):
        choice = str(input("Write action (buy, fill, take, remaining, exit): "))
        if choice == self.actions[0]:
            self.Buy()
        elif choice == self.actions[1]:
            self.Fill()
        elif choice == self.actions[2]:
            self.Take()
        elif choice == self.actions[3]:
            self.Remaining()
        elif choice == self.actions[4]:
            self.Exit()

    def Buy(self):
        choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino; 0 - Back: "))
        if choice == 1:
            self.Check(250, 0, 16, 4)
        elif choice == 2:
            self.Check(350, 75, 20, 7)
        elif choice == 3:
            self.Check(200, 100, 12, 6)
        elif choice == 0:
            self.Action()

    def Check(self, water_per_cup, milk_per_cup, beans_per_cup, price):
        if self.water - water_per_cup >= 0:
            self.water -= water_per_cup
        else:
            print("Sorry, not enough water!")
            self.Action()

        if self.milk - milk_per_cup >= 0:
            self.milk -= milk_per_cup
        else:
            print("Sorry, not enough milk!")
            self.Action()

        if self.beans - beans_per_cup >= 0:
            self.beans -= beans_per_cup
        else:
            print("Sorry, not enough coffee beans!")
            self.Action()

        if self.cups - 1 >= 0:
            self.cups -= 1
        else:
            print("Sorry, not enough cups!")
            self.Action()

        self.money += price
        print("I have enough resources, making you a coffee!")
        self.Action()

    def Fill(self):
        water_filling = int(input("Write how many ml of water you want to add: "))
        milk_filling = int(input("Write how many ml of milk you want to add: "))
        coffee_beans_filling = int(input("Write how many grams of coffee beans you want to add: "))
        cups_filling = int(input("Write how many disposable coffee cups you want to add: "))

        self.water += water_filling
        self.milk += milk_filling
        self.beans += coffee_beans_filling
        self.cups += cups_filling

        self.Action()

    def Take(self):
        print("I gave you {}".format(self.money))
        self.money = 0
        self.Action()

    def Remaining(self):
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        {} of money
        """.format(self.water, self.milk, self.beans, self.cups, self.money))
        self.Action()

    @staticmethod
    def Exit():
        print("Exit from machine...")


instance = CoffeeMachine(400, 540, 120, 9, 550, ["buy", "fill", "take", "remaining", "exit"])
instance.Action()

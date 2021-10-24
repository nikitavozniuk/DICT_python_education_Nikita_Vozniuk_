water_for_cup = 200
milk_for_cup = 50
coffee_beans_for_cup = 15

cups_of_coffee = int(input("Write how many cups of coffee you will need: "))
print("""For {} cups of coffee you will need:
{} ml of water
{} ml of milk
{} g of coffee beans""".format(
    cups_of_coffee,
    cups_of_coffee * water_for_cup,
    cups_of_coffee * milk_for_cup,
    cups_of_coffee * coffee_beans_for_cup
))

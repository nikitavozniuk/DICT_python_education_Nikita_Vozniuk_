bot_name = "Amazing ChatBot"
birth_year = 2021

print("Hello! My name is {}".format(bot_name))
print("I was created in {}".format(birth_year))

print("Please, remind me your name.")
name = str(input())
print("What a great name you have, {}!".format(name))

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {}; that's a good time to start programming!".format(age))

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

print("Now I will prove to you that I can count to any number you want.")
number = int(input())

for i in range(number+1):
    print("{} !\n".format(i))

print("Completed, have a nice day!")

print("Let's test your programming knowledge.")
print("""
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
""")


def test():
    input_number = int(input())
    if input_number == 2:
        print("Congratulations, have a nice day!")
        return
    else:
        print("Please, try again.")
        test()


test()

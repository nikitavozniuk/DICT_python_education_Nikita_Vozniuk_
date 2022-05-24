from math import radians
import random
import operator

num1 = random.randint(2, 9)
num2 = random.randint(2, 9)

success = "Right!"
fail = "Wrong!"

ops_list = ["+", "-", "*"]

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
}

rand_op = random.choice(ops_list)

correct_answer = ops[rand_op](num1, num2)

print(f"{num1}{rand_op}{num2}")
input_number = int(input())

if (input_number == correct_answer):
    print(success)
else:
    print(fail)

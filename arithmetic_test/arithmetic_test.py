import random
import operator

tries = 5
count = 0
correct = 0

success = "Right!"
fail = "Wrong!"
type_fail = "Incorrect format."
end_message = "Your mark is"

ops_list = ["+", "-", "*"]

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
}

while tries > count:
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    rand_op = random.choice(ops_list)
    correct_answer = ops[rand_op](num1, num2)

    print(f"{num1} {rand_op} {num2}")
    
    try:
        input_number = int(input())

        if (input_number == correct_answer):
            print(success)
            correct += 1
            count += 1
        else:   
            print(fail)
            count += 1
    except ValueError:
        print(type_fail)

print(f"{end_message} {correct}/{tries}")

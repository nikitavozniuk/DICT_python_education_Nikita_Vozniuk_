import os
import random
import operator

success = "Right!"
fail = "Wrong!"
type_fail = "Incorrect format."
end_message = "Your mark is"
end_message_ext = "Would you like to save the result? Enter yes or no."
name_text = "What is your name? "
file_save = 'The results are saved in "results.txt".'

levels = {
    1: "simple operations with numbers 2-9",
    2: "squaring numbers from 11 to 29"
}

start_message = """
Which level do you want? Enter a number: 
1 - simple operations with numbers 2-9 
2 - integral squares of 11-29
"""

ops_list = ["+", "-", "*"]

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
}

class ArithmeticTest:
    difficultyLevel = 0
    tries = 5
    count = 0
    correct = 0

    def setDifficultyLevel(self, value):
        self.difficultyLevel = value

    def generateSimpleRandomNumbers(self):
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)

        return [num1, num2]

    def generateSimpleRandomOp(self):
        return random.choice(ops_list)

    def generateSimpleCorrectAnswer(self, nums, op):
        return ops[op](nums[0], nums[1])

    def generateAdvancedRandomNumber(self):
        return random.randint(11, 29)

    def generatAdvancedCorrectAnswer(self, value):
        return value ** 2

    def checkCorrect(self, answer):
        try:
            input_number = int(input())

            if (input_number == answer):
                print(success)
                self.correct += 1
                self.count += 1
            else:   
                print(fail)
                self.count += 1
        except ValueError:
            print(type_fail)

    def start(self):
        while self.difficultyLevel == 0:
            try:
                choice = int(input(start_message))
                if choice == 1 or choice == 2:
                    self.setDifficultyLevel(choice)
                    self.loop()
            except ValueError:
                print(type_fail)
    
    def loop(self):
        while self.tries > self.count:
            if self.difficultyLevel == 1:
                nums = self.generateSimpleRandomNumbers()
                rand_op = self.generateSimpleRandomOp()
                answer = self.generateSimpleCorrectAnswer(nums, rand_op)

                print(f"\n{nums[0]} {rand_op} {nums[1]}")

                self.checkCorrect(answer)
            if self.difficultyLevel == 2:
                number = self.generateAdvancedRandomNumber()
                answer = self.generatAdvancedCorrectAnswer(number)

                print(number)

                self.checkCorrect(answer)
        print(f"{end_message} {self.correct}/{self.tries}. {end_message_ext}")
        choice = input()

        if choice == "yes":
            name = input(name_text)

            f = open(os.path.join("arithmetic_test", "results.txt"), "a")
            f.write(f"{name}: {self.correct}/5 in level {self.difficultyLevel} ({levels[self.difficultyLevel]}).\n")
            f.close()


arithmetic_test = ArithmeticTest()
arithmetic_test.start()

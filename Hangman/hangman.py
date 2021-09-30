import random

print("""
HANGMAN
The game will be available soon.
""")

words = ["python", "java", "javascript", "php", "c++"]
word = random.choice(words)


def start():
    attempts = 8
    guess = word.replace(word, "-" * len(word))
    while word != guess:
        if attempts == 0:
            return

        guess_list = list(guess)
        print(guess)
        letter = str(input("Input a letter: "))

        if letter not in word:
            print("That letter doesn't appear in the word")
        else:
            for index, item in enumerate(word):
                if letter == item:
                    guess_list[index] = item
                    guess = "".join(guess_list)
        attempts -= 1


start()
print("Thanks for playing!")
print("We'll see how well you did in the next stage")

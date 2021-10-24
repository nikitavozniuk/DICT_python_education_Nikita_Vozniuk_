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
            print("You lost!")
            return

        guess_list = list(guess)
        print(guess)
        letter = str(input("Input a letter: "))

        if letter not in word:
            print("That letter doesn't appear in the word")
            attempts -= 1
        else:
            if letter in guess:
                print("No improvements")
                attempts -= 1
            else:
                for index, item in enumerate(word):
                    if letter == item:
                        guess_list[index] = item
                        guess = "".join(guess_list)
    if "-" not in guess:
        print(guess)
        print("You guessed the word!")
        print("You survived!")
        return


start()
# print("Thanks for playing!")
# print("We'll see how well you did in the next stage")

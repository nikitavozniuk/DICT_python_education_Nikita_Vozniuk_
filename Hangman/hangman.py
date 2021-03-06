import random

print("""
HANGMAN
""")

words = ["python", "java", "javascript", "php"]
word = random.choice(words)


def game_loop():
    command = str(input('Type "play" to play the game, "exit" to quit: '))
    if command == "play":
        start()
    elif command != "quit":
        game_loop()
    else:
        return


def start():
    attempts = 8
    guess = word.replace(word, "-" * len(word))
    all_guessed = []
    while word != guess:
        if attempts == 0:
            print("You lost!")
            game_loop()

        guess_list = list(guess)
        print(guess)
        letter = str(input("Input a letter: "))

        if letter.isalpha() and letter.islower():
            if len(letter) != 1:
                print("You should input a single letter.")
            else:
                if letter not in word:
                    print("That letter doesn't appear in the word")
                    all_guessed.append(letter)
                    attempts -= 1
                else:
                    if letter in guess:
                        print("You've already guessed this letter.")
                    elif letter in all_guessed:
                        print("You've already guessed this letter.")
                    else:
                        for index, item in enumerate(word):
                            if letter == item:
                                guess_list[index] = item
                                guess = "".join(guess_list)
        else:
            print("Please enter a lowercase English letter.")
    if "-" not in guess:
        print(guess)
        print("You guessed the word!")
        print("You survived!")
        game_loop()


game_loop()

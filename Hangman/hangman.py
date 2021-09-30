import random

print("""
HANGMAN
The game will be available soon.
""")

words = ["python", "java", "javascript", "php", "c++"]
word = random.choice(words)

answer = str(input("Guess the word: "))

if answer == word:
    print("You survived!")
else:
    print("You lost!")

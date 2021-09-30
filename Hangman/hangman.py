import random

print("""
HANGMAN
The game will be available soon.
""")

words = ["python", "java", "javascript", "php", "c++"]
word = random.choice(words)
hint = word[:3] + "-" * (len(word) - 3)

answer = str(input("Guess the word {}: ".format(hint)))

if answer == word:
    print("You survived!")
else:
    print("You lost!")

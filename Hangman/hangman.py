print("""
HANGMAN
The game will be available soon.
""")

word = "dict"
answer = str(input("Guess the word: "))

if answer == word:
    print("You survived!")
else:
    print("You lost!")

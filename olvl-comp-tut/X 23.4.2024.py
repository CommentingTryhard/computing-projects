import random

words = ["apple", "banana", "chocolate"]
word = random.choice(words)

lives = 3
guessed = ["_" for x in word]

while "".join(guessed) != word:
    print("".join(guessed))
    letter = input("Enter a letter to guess: ")
    if letter in word:
        print("{} was in the word!".format(letter))
        guessed = [(x if (x == letter or letter != "_") else "_") for x in guessed]
    else:
        print("{} was not in the word. {} lives left!".format(letter, lives))
        lives -= 1
        if lives <= 0:
            print("Game over!")
            break
    

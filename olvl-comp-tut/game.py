"""
1. Create a program that collect 5 colours from a person, these colors must be a choice from red, yellow, green, blue, black, white, cyan, pink.You require validation
2. Program will randomly select 3 colours and will put into a secret list.
3. Invite the player to key in the list of 3  colors, ensuring the color and the index position must match the secret list.
4. Each time, if it matches, program will identify the position so that the next try the player can make use of this information.
5. Player has up to 5 tries to finish trying the colours combinations. 

Your game when programmed should be logical to play. So a lot of details up to you .
"""
import random as r


dbtb = ["red", "yellow", "green", "blue", "black", "white", "cyan", "pink"]
secretlist = []
lists = []
inputtedlist = []
counter = 0
counters = 0
while counter<5:
    colour = input("Please input your colour: ")
    colour = colour.lower()
    if colour in dbtb:
        lists.append(colour)
        counter+=1
    else:
        print("Please reenter your input.")
for i in range(3):
    choices = r.choice(lists)
    secretlist.append(choices)

print("Your format for the question should be in one word per input")
while counters<3:
    inputs = input("Pleae enter your word: ")
    for o in inputs:
        if (o == " ") or (o == "."):
            inputtedlist.append(inputs)
            counters+=1
        else:
            print("Please reenter your input.")
if inputtedlist == secretlist:
    
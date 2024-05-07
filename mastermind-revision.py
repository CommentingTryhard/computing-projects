"""
Exam Question:

You are tasked with coding a two-player version of the Mastermind game with the following variations:

Repeated Colors:
Allow repeated colors in the hidden sequence and the player's guesses.
Two-player Mode:
Implement a two-player mode where each player takes turns being the code maker and the code breaker.
After one round, the players should have the option to play again or quit the game.
Scoring System:
Implement a scoring system based on the number of attempts taken by the code breaker to guess the sequence.
Award points based on the difficulty level chosen.
Your task is to write a Python program that incorporates these variations. Your program should:

Allow two players to take turns playing as the code maker and the code breaker.
Accept repeated colors in the hidden sequence and the player's guesses.
Implement a scoring system based on the number of attempts taken by the code breaker to guess the sequence.
Award points based on the difficulty level chosen.
"""
import time

leaderboard = #2d matrix
# Player1 and Player2
userlist = []
funny = "..."
funny2= "   "

"""
game plan:
    - Build a basic GUI for player 1 and 2, let p1 go and select its code, then let p2 start guessing
"""
if len(userlist) == 0:
    print("Creating new user", end = "")
    for i in range(3):
        print(funny2[i]+funny[i])
else:
    print("Please sign")

print("Welcome {}")
GUIinputs = input("Please input your choices: ")

user = input("Create a new user on the terminal: ")

"""
import time
funny = "..."
funny2= "   "
time.sleep(1)
print("Creating new user", end = "")
for i in range(3):
    time.sleep(1)
    print(funny2[0:i]+funny[i], end = "")
    time.sleep(1)
"""
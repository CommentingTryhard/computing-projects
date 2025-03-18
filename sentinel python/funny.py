import time
import random


flag = True
def load():
    for i in range(25):
        time.sleep(0.1)
        print("-", end = "")
    for i in ["L","0","A","D","1","N","G"]:
        time.sleep(0.1)
        print(i, end = "")
    for i in range(25):
        time.sleep(0.1)
        print("-", end = "")
def stringing(string):
    for i in string:
      time.sleep(0.1)
      print(i, end = "")
        
load()
print("\nLoading complete. Welcome, new player.\n")
name = input("Please input your name: ")
stringing(name)
print("\n")
load()
stringing("\nOnce upon a time, a hunter appeared in the woods looking to setup camp.\n")
while flag:
    fork = input("Would you like to setup camp or enter the forest? (A/B): ")
    if fork.lower() == "a":
        flag = False
        stringing("\nYou decide to head out at night, trying to explore the forest ahead of you.")
    elif fork.lower() == "b":
        flag = False
        stringing("\nAs you setup camp, you realise that you require logs for camp. By morning, you decide to head out.")
    else:
        stringing("\nOption is not recognised!")
        
#fork
stringing("\nYou encounter a fork in the path within the forest. One leads to a river, the other leads to a dark cave.")
flag = True
while flag:
    fork = input("\nWould you like to enter the dark cave, or venture towards the river? (A/B): ")
    if fork.lower() == "a":
        flag = False
        print("\n")
        load()
        stringing("\nYou venture towards the dark cave, and you discover a sleeping dragon within the cave.")
        stringing("\nYou see traces of gold at the heart of the sleeping dragon.")
        fork = input("Would you like to try and steal the dragon's treasure, or trek around it and search the rest of the cave? (A/B): ")
        flag = True
        while flag:
            if fork.lower() == "a":
                flag = False
                chance = random.randint(1,9)
                if chance > 6:
                    stringing("\nYou manage to steal the dragon's treasure, and escape in one piece. Congrats!")
                    break
                elif chance > 4:
                    stringing("\nYou managed to steal the dragon's treasure, but failed to escape in one piece, suffering injuries in the battle.")
                    break
                else:
                    stringing("\nYou did not manage to steal the dragon's treasure, and additionally pissed it off. You have lost.")
                    break
            elif fork.lower() == "b":
                flag = False
                chance = random.randint(1,9)
                if chance > 6:
                    stringing("\nYou manage to find the treasure, and escape in one piece. Congrats!")
                    break
                else:
                    stringing("\nYou did not manage to steal the treasure, and additionally pissed the dragon off. You have lost.")
                    break
            else:
                stringing("\nOption is not recognised!")
    elif fork.lower() == "b":
        flag = False
        print("\n")
        load()
        stringing("\nAs you move nearer to the river, the sounds of rushing water fill your ears.\n")
        stringing("\nYou realise that it is extremely difficult to swim across.")
        fork = input("Would you like to try and swim across the river or construct a raft to travel across? (A/B): ")
        flag = True
        while flag:
            if fork.lower() == "b":
                flag = False
                chance = random.randint(1,9)
                if chance > 6:
                    stringing("\nYou manage to find enough materials to construct your raft, and swim across. Who knows what you will find across the river?")
                    break
                elif chance > 4:
                    stringing("\nYou manage to find enough materials for your raft, but can not survive the viscious waves of the river. ")
                    break
                else:
                    stringing("\nAs you were gathering materials for your raft, dumb luck strikes as the dragon, awakes from its thousand-year slumber, looking for a snack. You are its first target of the day, unlucky. You have lost.")
            elif fork.lower() == "a":
                flag = False
                chance = random.randint(1,9)
                if chance > 6:
                    stringing("\nAs you swim, you encounter a underwater cave with an air bubble. You decide to explore the underwater cave.")
                    stringing("\nYou manage to find the treasure, and escape in one piece. Congrats!")
                    break
                else:
                    stringing("\nAs you swim, you did not find a way across, and eventually drown within the viscious waves of the river.")
                    stringing("\nYou did not manage to find the treasure. You have lost.")
                    break
            else:
                stringing("\nOption is not recognised!")
        
    else:
        stringing("\nOption is not recognised!")
from colourist import Color
import time
def prints(string):
    for i in string:
        print(i, end="")
        time.sleep(0.1)
    print(end=" ")

prints("Welcome to this tutorial on searches and algorithms.".format(Color.CYAN))




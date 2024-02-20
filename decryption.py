import random as r

seclist = []

#encryption letters:
"""
a) key = len(1)
b) key = len(any)
"""

secret = input("Enter your secret sentence: ")
key = int(input("Please input your key: "))

encrypted = ""
chooser = input("Would you like to encrypt or decrypt:(E/D) ")
if (chooser == "E") or (chooser == "e"):
    for i in secret:
        seclist.append(i)
    for letter in seclist:
        if letter in "!@#$%^&*()<>?:,./;'[]\`~|_+":
            pass
        else:    
            lend = ord(letter)+key
            if lend < 123:
                newletter = chr(ord(letter)+key)
                letter = newletter
            if lend > 122:
                orde = lend-27
                newletter = chr(ord("a")+orde)
                letter = newletter 
    print(seclist)
    print(*seclist)        
elif (chooser == "d") or (chooser == "d"):
    pass

else:
    print("Your letter was not able to be identified.")
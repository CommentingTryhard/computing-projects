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
    print(seclist)
    for index, value in enumerate(seclist):
        print(value)
        if value in "!@#$%^&*()<>?:,./;'[]\`~|_+":
            pass
        else:    
            lend = ord(value)+key
            if lend < 123:
                newletter = chr(ord(value)+key)
                seclist.pop(index)
                seclist.insert(index, newletter)
            if lend > 122:
                orde = lend-26
                newletter = chr(orde)
                seclist.pop(index)
                seclist.insert(index, newletter)
    print(seclist)
    for i in ():
        if i == " ":
            seclist.replace(i,"")
elif (chooser == "d") or (chooser == "d"):
    pass

else:
    print("Your letter was not able to be identified.")
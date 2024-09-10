import random as r

seclist = []

#encryption letters:
"""
a) key = len(1)
b) key = len(any)
"""

"""
plan:
when statement is inputted:
key*ord(i)

"""

secret = input("Enter your secret sentence: ")
key = int(input("Please input your key: "))

encrypted = ""
chooser = input("Would you like to encrypt or decrypt:(E/D) ")
if (chooser == "E") or (chooser == "e"):
    for i in secret:
        seclist.append(i)
    for index, value in enumerate(seclist):
        if value in "!@#$%^&*()<>?:,./;'[]\`~|_+":
            pass
        elif value.islower():  
            lend = ord(value)+key
            if lend < 123:
                orde = lend
                #break in
                ordelist = []
                pissorde = orde*key
                if len(str(pissorde))%2!=0:
                    orde = str(pissorde)+"1"
                else:
                    orde = pissorde
                for i in str(orde):
                    ordelist.append(i)
                for inx, value in enumerate(ordelist):
                    if (inx+1)%2!=0:
                        newletter = chr(int(ordelist[inx]+ordelist[inx+1]))
                        seclist.insert(index+1, newletter)
                    else:
                        pass
                seclist.pop(index)
            if lend > 122:
                orde = lend-26
                #break in
                ordelist = []
                pissorde = orde*key
                if len(str(pissorde))%2!=0:
                    orde = str(pissorde)+"1"
                else:
                    orde = pissorde
                for i in str(orde):
                    ordelist.append(i)
                for inx, value in enumerate(ordelist):
                    if (inx+1)%2!=0:
                        newletter = chr(int(ordelist[inx]+ordelist[inx+1]))
                        seclist.insert(index+1, newletter)
                    else:
                        pass
                seclist.pop(index)
        elif value.isupper():
            lend = ord(value)+key
            if lend < 91:
                orde = lend
                #break in
                ordelist = []
                pissorde = orde*key
                if len(str(pissorde))%2!=0:
                    orde = str(pissorde)+"1"
                else:
                    orde = pissorde
                for i in str(orde):
                    ordelist.append(i)
                for inx, value in enumerate(ordelist):
                    if (inx+1)%2!=0:
                        newletter = chr(int(ordelist[inx]+ordelist[inx+1]))
                        seclist.insert(index+1, newletter)
                    else:
                        pass
                seclist.pop(index)
            if lend > 90:
                orde = lend+26
                #break in
                ordelist = []
                pissorde = orde*key
                if len(str(pissorde))%2!=0:
                    orde = str(pissorde)+"1"
                else:
                    orde = pissorde
                for i in str(orde):
                    ordelist.append(i)
                for inx, value in enumerate(ordelist):
                    if (inx+1)%2!=0:
                        newletter = chr(int(ordelist[inx]+ordelist[inx+1]))
                        seclist.insert(index+1, newletter)
                    else:
                        pass
                seclist.pop(index)
    seclist = "".join(seclist)
    print(seclist)
elif (chooser == "D") or (chooser == "d"):
    for i in secret:
        seclist.append(i)
    for index, value in enumerate(seclist):
        if value in "!@#$%^&*()<>?:,./;'[]\`~|_+":
            pass
        elif value.islower():  
            lend = ord(value)-key
            if lend > 96:
                newletter = chr(ord(value)-key)
                seclist.pop(index)
                seclist.insert(index, newletter)
            if lend < 97:
                orde = lend+26
                newletter = chr(orde)
                seclist.pop(index)
                seclist.insert(index, newletter)
        elif value.isupper():
            lend = ord(value)-key
            if lend < 91:
                newletter = chr(ord(value)-key)
                seclist.pop(index)
                seclist.insert(index, newletter)
            if lend > 90:
                orde = lend-26
                newletter = chr(orde)
                seclist.pop(index)
                seclist.insert(index, newletter)
    seclist = "".join(seclist)
    print(seclist)

else:
    print("Your letter was not able to be identified.")
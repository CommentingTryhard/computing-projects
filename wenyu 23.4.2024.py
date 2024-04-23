import random

wordbank = ["babies", "packed", "eagles", "labels", "oafish", "iambus", "pacify"]
flag = True
chances = 5
wordguess = False
flag1 = True

def choose1():
    letterbank = []
    printedlist = []
    flist = []
    while flag1:
        word = input("Please input your word: ")
        if word.isalpha():
            flag1 = False
            for i in word:
                letterbank.append(i)
        else:
            print("Please reenter your word.")
    while chances != 0 or wordguess:
        characterinput = input("Please input your letter guess: ")
        for i in len(letterbank):
            printedlist.append("_")
        for h in letterbank:
            if characterinput == ih:
                indext = h.index()
                flist.append(indext)
        for ij in flist:
            wordtoreplace = printedlist[ij]
            printedlist.replace(wordtoreplace, characterinput)
        chances-=1
        "".join(printedlist)
        print(printedlist)
        print("You have {} chances left.".format(chances))
        
            
while flag:
    choice = input("Please enter if you would like to choose your own word, or from a wordbank: (1/2): ")
    if choice == "1":
        flag = False
        choose1()
        
    elif choice == "2":
        flag = False
        choose2()
    else:
        print("Your choice sucks.")
    
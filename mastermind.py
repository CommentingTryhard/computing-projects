hiddenlist = []
choicelist = []
counterlist = ["1","2","3","4"]
flag = False
wordguess = False

print("Welcome to Mastermind. Player 1 will start first.")
print("Please choose your corresponding difficulty: ")
difficulty = input("Please input your difficulty: (easy/medium/hard) ")
if difficulty.lower() == "easy":
    chances = 15
elif difficulty.lower() == "medium":
    chances = 10
elif difficulty.lower() == "hard":
    chances = 5
else:
    print("Your answers suck and you suck alot.")
    del all
print("As player 1, you will select 4 colours in 4 index positions.")
for i in range(4):
    colour = input("Please input your colour, 1 at a time. Your colour will be placed in an ascending order: ")
    hiddenlist.append(colour)

print("Please pass the console to player 2.")
while chances !=0 or wordguess == False:
    for i in range(4):
        colourchoice = input("Please input your colour choice: ")
        choicelist.append(colourchoice.lower())
    for index, value in enumerate(colourchoice):
        if value == hiddenlist[index]:
            print("{} Green".format(index+1))
            counterlist.replace(str(index), "Green")
        else:
            print("{} Red.".format(index+1))

    chances-=1
    for i in counterlist:
        if i == "Green":
            flag = True
        elif i in "1234":
            flag = False
    if flag == False:
        wordguess == False
    else:
        wordguess == True
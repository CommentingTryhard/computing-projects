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
    SystemExit
print("As player 1, you will select 4 colours in 4 index positions.")
for i in range(4):
    colour = input("Please input your colour, 1 at a time. Your colour will be placed in an ascending order: ")
    hiddenlist.append(colour)

print("Please pass the console to player 2.")
while chances !=0 or wordguess == False:
    for i in range(4):
        colourchoice = input("Please input your colour choice: ")
        choicelist.append(colourchoice.lower())
    for index, value in enumerate(choicelist):
        if str(value) == str(hiddenlist[index]):
            print("{} Green".format(index+1))
            counterlist[index] = "Green"
        else:
            print("{} Red.".format(index+1))
    for i in counterlist:
        if i == "Green":
            flag = True
        elif i in "1234":
            flag = False
    if flag == False:
        wordguess = False
    else:
        wordguess = True
    chances-=1

if wordguess == True:
    print("Congratulations! You have correctly guessed the order!")
    print("The order is {}".format(hiddenlist))
else:
    print("You have not guessed the hidden colours, here are the results. {}".format(hiddenlist))

print("Thanks for playing!")
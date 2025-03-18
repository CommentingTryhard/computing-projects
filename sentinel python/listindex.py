invites_list = ["Max", "Marta", "Mose", "Mona", "Margarita", "Mike"]
flag = True
while flag:
    strinput = input("Please enter a name: (n to quit) ").title()
    if strinput == "n":
        flag = False
        break
    if strinput in invites_list:
        print(strinput)
        print("{} is invited to the party!".format(strinput))
    else:
        print("{} is not invited to the party, sorry.".format(strinput))
        indexinput = int(input("Please input your index to replace: "))
        print("{} will replace {}".format(strinput, invites_list[indexinput]))
        invites_list[indexinput] = strinput

flag1 = True
emaillist = []
printedlist = []
while flag1:
    email = input("Please input your email: ")
    if "@" in email:
        if email[-8:-1] == ".edu.sg":
            emaillist.append(email)
        else:
            print("no2")
    else:
        print("no1")
    if email == "QUIT":
        flag1=False


for o in emaillist:
    if o not in printedlist:
        printedlist.append([o,1])
    elif o in printedlist:
        for p in printedlist:
            if o == p:
                p[1]+=1
            else:
                pass
    else:
        print("big error")
    
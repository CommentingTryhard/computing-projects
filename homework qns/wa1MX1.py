flag = True
listnum = []

while flag:    
    prompt = input("Please input 5 numbers seperated by space: ")
    prompt = prompt.split(" ")
    print(prompt)
    for i in prompt:
        if i.isdigit():
            if (int(i)>=10) or (int(i)<=99):
                if len(prompt) == 5:
                    flag = False
                    print("debug1")
                    break
                else:
                    print("pls reprompt thanks")
            else:
                print("pls repmrompt thank")
        else:
            print("pls reprompt tks")
print("debug2")
if flag == False:
    for i in prompt:
        prompta = int(i)
        listnum.append(prompta)
    ops = sum(listnum)
    if (ops%10 == 0):
        print("CHEKSUM LIMKA SUCCESS")
    else:
        print("uu need help")
else:
    #i forgot whats this
    print("yes")
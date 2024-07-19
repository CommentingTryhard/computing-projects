counter=0
wordlist = [["X1","ice-cream"],
            ["Y2","formatting"],
            ["Z1","dressing"]]
for i in wordlist:
    print(i[0])
    print(i[1][-2:])
while counter<2:
    value = input("Please input the value: ")
    for i in wordlist:
        if value == i[0]:
            print(i[1])
            counter+=1
        else:
            pass
            
        
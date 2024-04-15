#q1
counter = 0
lista = ["pig","giraffe","cow"]
listb = []
while (counter<5):
    inputs = input("Please input your animal: ")
    if inputs.lower() in lista:
        counter+=1
        listb.append(inputs)
    else:
        print("no")
print(listb)

#q2
numlist2 = []
numlist = []
flag = True
while flag:
    num = input("Please input your number: ")
    if len(num)==3:
        for i in str(num):
            numlist.append(int(i))
        if sum(numlist)%2 == 0:
            print("no")
        else:
            numlist2.append(num)
    elif num.lower() == "quit":
        flag = False
        print(numlist2)
    else:
        print("no")

#q3
paralist = []
def word(parameter):
    if parameter.isalpha() == True:
        for i in parameter:
            paralist.append(ord(i))
            return paralist
    else:
        return False

def reversing(list):
    for i in list:
        

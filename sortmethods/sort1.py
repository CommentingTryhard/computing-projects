counter = 0
listnum = []
list2 = []

while counter<5:
    num = int(input("Please add in your number: "))
    counter+=1
    listnum.append(num)
    
def unique_sort(listofnum):
    for i in listofnum:
        if i in list2:
            pass
        else:
            list2.append(i)
    return list2
    
unique_sort(listnum)

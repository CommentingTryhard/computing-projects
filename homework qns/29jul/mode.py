numlist = []
for i in range(10):
    number = int(input("Enter a number: "))
    numlist.append(number)
print("The original list is: {}".format(numlist))

numlist.sort()  
print("The sorted list is: {}".format(numlist))  

mode = numlist[0]
highestfrequency = 1
frequency = 1

for i in range(len(numlist)-1):
    if numlist[i+1] == numlist[i]:
        frequency +=1
    else:
        frequency = 1
        
    if frequency > highestfrequency:
        highestfrequency = frequency
        mode = numlist(i)
    
print("The mode is {}.".format(mode))
print("The highest frequency of mode is {}.".format(highestfrequency))
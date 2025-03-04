import numpy

#Q1

neword = []
palindrome = input("Enter a string: ")
for i in range(len(palindrome)):
    neword.append(palindrome[-i-1])
neword = "".join(neword)
if neword == palindrome:
    print("Yes")
else:
    print("No")

#Q2

counter = 0
counter2 = 0
intlist = []
int2list = []
int3list = []
for i in range(int(input("Please input how many numbers: "))): 
    inte = int(input("Please input the numbers you want: "))
    intlist.append(inte)
    
for i in intlist:
    counter+=1
    if counter%2==0:
        int2list.append(i)
print(sum(int2list))

for i in intlist:
    counter2+=1
    if counter2%2!=0:
        int3list.append(i)
print(numpy.prod(int3list))

#Q6

num = int(input("Please input your square number: "))


print("n = {}".format(num))
for i in range(3):
    print("{} * {} = {}".format(num+i,num+i,(num+i)**2))

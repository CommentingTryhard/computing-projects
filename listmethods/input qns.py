counter = 0
flag = True
lista= []
vowel = "AEIOUaeiou"
vcount = 0
opscount = 0
ops2count=0
xindex = []
yindex = []

while flag:
    if counter==0:
        ops = input("Please input your letter: ")
        if ops.isalpha():
            lista.append(ops)
            counter+=1
        else:
            pass
    elif counter==1:
        ops2 = input("Please input your second letter: ")
        if ops2.isalpha():
            if (ops2 != ops):
                lista.append(ops2)
                counter+=1
            else:
                print("Please input a letter that differs from the first.")
                pass
        else:
            print("Please input a lettter.")
            pass
    elif counter==2:
        flag = False
        
sen = input("Please input your sentence: ")
for i in sen:
    if i in vowel:
        vcount+=1
    if i in ops:
        opscount+=1
    if i in ops2:
        ops2count+=1
        
for index, value in enumerate(sen):
    if value == ops:
        xindex.append(index)
    if value == ops2:
        yindex.append(index)
        
print("Number of vowels: {}".format(vcount))
print("Number of letter x: {}  Number of letter y: {}".format(opscount, ops2count))
print("Index position of x are: {}".format(xindex))
print("Index position of y are: {}".format(yindex))
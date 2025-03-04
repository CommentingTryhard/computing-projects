#x is your lilst.

def func(x):
    for value, index in enumerate(x):
        if index%2==0:
            x = x.pop[index]
    print(x)
            
#x and y will be your variable names for each list  

def func(x,y):
    numlist = []
    if len(x) > len(y):
        x = x[:3]
    for counter in range(len(x)):
        suma = x[counter]+y[counter]
        numlist.append(suma)
    print(sum(numlist))

#define your x and y as list variables.

def func(x,y):
    for i in x:
        for o in y:
            if i ==o:
                return True
            else:
                pass
                flag = False
    if flag == False:
        return False

#you need to use random library to generate random numbers/choices.
#random.choice(x)

def func(numlist):
    numlist.sort()
    print(numlist[0])

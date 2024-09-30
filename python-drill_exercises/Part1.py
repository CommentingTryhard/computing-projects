def count_even_numbers(lst):
    rtnlist = []
    for i in lst:
        if i%2==0:
            rtnlist.append(i)
    return rtnlist

def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

def sum_of_digits(n):
    lst = []
    n = str(n)
    for i in n:
        lst.append(int(n))
    return sum(lst)

def reverse_strings(s):
    rtnlist = []
    for i in s:
        rtnlist.append(-1, i)
    return rtnlist

def factorial(n):
    counter = n
    sum = 1
    while counter!=0:
        counter-=1
        sum = sum*counter
    return sum

def q6(lst):
    rtnlst = []
    for index, value in enumerate(lst):
        if index%2==0:
            rtnlst.append(value)
    print(rtnlst)

def q7(numlist):
    for i in numlist:
        if i<0:
            return False
    return True

def fibonacci(n):
    sum1 = 0
    sum = 1
    for i in range(n):
        sum1 = sum
        sum = sum1+sum-1
        print(sum)

def largest_in_list(lst):
    top = lst[0]
    for i in lst:
        if i>=top:
            top = i
        else:
            pass
    return top

def retn():
    num = 0
    while num<=100:
        num = int(input("Please input your number: "))   
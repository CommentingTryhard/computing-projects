mixed = [10, 12, "Mimi", 17, 3.14, "Bobo"]

print(len(mixed))
    
print(mixed[2])

#create a numlist fro ma range of 10 t0 30

numlist = list(range(10,31))
numix = [10,24,52,15,8,4,7,12,6,0.1]
print(min(numix))

#num2

num2 = [10,11,13,16,17,18]
num2.insert(2,12)
num2.insert(4,14)
num2.insert(5,15)
num2.insert(9,19)
print(num2)

#num3
num3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(num3[-3])


#exercise
"""
create a program that ask a person how many numbers he will input
put in list
print out sum
print out last numba
"""
numlist = []

for i in range(3):
    word = int(input("Please write dey numba: "))
    numlist.append(word)

print(sum(numlist))
print(numlist[-1])

#exercise2

num5 = [11,13,15,17,18,11,14,12,13,17,14,16,18,19,14]
numlist = []
numlist2 = []
for i in num5:
    if num5.count(i) > 1:
        numlist.append(num5.count(i))
        if num5.count(i) in numlist:
            pass
            if num5.count(i) in numlist:
                num5.count(i).pop
            else:
                numlist2.append(num5.count(i))
        else:
            break
    else:
        pass
print(numlist2)

#extend

num1 = [1,2,3,4,6,7,8]
num2 = [10,11,12,14,15]

num1.extend(num2)
print(num1)

numbers = [1,5,3,7,4,9,8,4,2]

#sort
numbers.sort()
print(numbers)

#sorted - maintain your original list and u create a new list based on sorted arrangement

numbers = [11,16,12,18,19,30,8,10]
numbersorted = sorted(numbers)
print(numbers)
print(numbersorted)

#reverse sorted

numbers = [11,16,12,18,19,30,8,10]
numbersorted = sorted(numbers, reverse = True)
print(numbersorted)

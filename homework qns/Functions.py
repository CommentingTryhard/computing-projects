def greeting():
    name = input("Please enter your name: ")
    print("Good Morning", name)
    
greeting()

def greeting(name = "People!"): 
#name will default to people if no input in line 12
    name = input("Please enter your name: ")
    print("Good Morning", name)
    
greeting()

def greeting(name = "People!"): #name will default to people if no input in line 5
    if len(name)<5:
        print("Good morning ",name,"you are SHORTASS BUDDY!")
    else:
        print("Good morning ",name,"you are too long")
        
greeting()

#print statements and return statements
#return statements help return the value to the function that calls for it
def sum1(a,b):
    a = int(input("Enter a value: "))
    b = int(input("Enter a value: "))
    return a+b
    
sum1(3,2)
def multiplier(c):
    return sum1()*c
    
multiplier(5)
#create 2 functions 
#f1 = diff between a and b
#f2 =  return f1, check whether %= 3/5

def f1():
    a = float(input("Please enter your input: "))
    b = float(input("Please enter your input: "))
    return abs(a-b)

def f2():
    diff = f1()
    if diff%3==0 or diff%5==0:
        print(diff)
    else:
        print("Not divisible by 3 or 5.")
f2()

def f1():
    name = list(input("Enter your name: "))
    print(name[:-1])
f1()

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""
program will take the shape and calculate the area 
3 shap: circle triangle coob
"""
import math
def shapes(n):
    
    def circle():
        r = float(input("enter the radius: "))
        area = math.pi * r**2
    def triangle():
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        area = one*b*h
    def cube():
        s = float(input("Enter side length: "))
        area = s**2*6
        
    if n == "circle":
        return circle()
    if n == "triangle":
        return triangle()
    if n == "cube":
        return cube()
        
print(shapes("circle"))

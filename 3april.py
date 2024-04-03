studentcolour = []
flag = True
def colourinput(studentcolour):
    while flag:
        colour = input("What is the student's favourite colour? ")
        cinput = input("Please enter if you would like to enter another colour (Y/N):")
        colour = colour.lower()
        studentcolour.append(colour)
        if cinput.lower() == "y":
            flag = True
        elif cinput.lower() == "n":
            flag = False
        else:
            print("I do not understand your input.")
    return studentcolour

def search_list(studentcolour):
    counter = 0
    colour = input("Please input the colour you want to search for: ")
    colour = colour.lower()
    for value in studentcolour:
        if value == colour:
            counter+=1
    print(counter)
    print(value)
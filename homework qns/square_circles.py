flag = True
def square_side(sq_perimeter):
    side_length = sq_perimeter / 4
    return side_length
    
def square_area(perimeters):
    perimeter = square_side(perimeters)
    area = perimeter**2
    return area

def circle_diam(circumference):
    diameter = circumference / 3.14
    return diameter

def circle_area(circumference):
    diameter = circle_diam(circumference)
    radius = diameter/2
    area = 3.14*(radius**2)
    return area

while flag:    
    shape = input("Please input what shape do you want to check for: ")
    if (shape.lower() == "square"):
        perimeter = int(input("Please input your perimeter: "))
        area = square_area(perimeter)
        print(area)
        flag = False
    elif (shape.lower() == "circle"):
        perimeter = int(input("Please input your perimeter: "))
        area = circle_area(perimeter)
        print(area)
        flag = False
    else:
        print("Please re-enter your shape.")



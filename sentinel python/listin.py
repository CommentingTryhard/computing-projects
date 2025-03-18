first = input("Please enter a first course (soup/salad): ")
second = input("Please enter a second course (noodles/curry): ")

dict = {
    "soup" : ["chicken broth", "noodles", "carrot", "celery"],
    "salad" : ["lettuce", "tomato", "cucumber", "olive oil"],
    "noodles" : ["noodles", "chicken", "peppers", "soy sauce"],
    "curry" : ["chicken", "curry powder", "coconut milk", "rice"]
}

holder = dict[first] + dict[second]
pep = []
for i in holder:
    if i in pep:
        pass
    else:
        pep.append(i)
print("The groceries are:\n{}".format(pep))
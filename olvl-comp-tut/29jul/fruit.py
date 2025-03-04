fruitlist = ["apple","orange","pear"]
stock = [1,1,1]
fruit = " "
while fruit != "":
    fruit = input("Enter fruit to add: ")
    if fruit.lower() in fruitlist:
        for i in fruitlist:
            if i == fruit:
                newstock = stock[i]+1
                stock.pop(i)
                stock.insert(i, newstock)
            else:
                fruitlist.append(fruit)
                stock.append("1")
print(fruitlist)
print(stock)
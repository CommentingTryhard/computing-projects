flag = True

while flag:
    byte = input("Please input your bits, with a space in between eact tetrahedral: ")
    if len(byte) ==9:
        if byte[0:3].isdigit() and byte[5:8].isdigit():
            if byte[4] == " ":
                print(byte)
                flag = False
                
#a guy invited to key in a number ata time, n wil stop if "q" is entered

letterlist = []
tru = True
while tru:
    theinput = int(input("Pls enter la letter: "))
    if str(theinput) == "q" or str(theinput) == "Q":
       letterlist.append(theinput)
    else:
        tru = False
        
sumofinput = sum(letterlist)
print(sumofinput)

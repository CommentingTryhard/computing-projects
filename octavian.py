namelist = []
for i in range(10):
    names = input("Please input your names: ")
    names = names.upper()
    namelist.append(names)
for i in namelist:
    firsltr = i[0]
    secltr = (i+1)[0]
    if ord(firsltr) > ord(secltr):
        orgword = namelist[i]
        namelist.pop[i+1]
        namelist.insert(i, orgword)
    else:
        pass
print("Please confirm and check the names above: {}".format(namelist))
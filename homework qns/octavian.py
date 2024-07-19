namelist = ["MARY","Jane","Lester","WILLIAM","calvIN","Henry","CHArles","JOLIET","COULSON","edison"]
numworth = [] 
"""
for i in range(10):
    names = input("Please input your names: ")
    names = names.upper()
    namelist.append(names)
"""
namelist.sort()

for i in namelist:
    ltr_worthlist = []
    numworth_list = []
    for ltr in i:
        ltr_worth = ord(ltr)
        ltr_worthlist.append(ltr_worth)
    num_worth = sum(ltr_worthlist)
    numworth_list.append(num_worth)
total_worth = sum(numworth_list)
print(total_worth)

sorted_list = sorted(namelist, key=len, reverse=True)
benchmark = len(sorted_list[0])
for i in sorted_list:
    if len(i) <= benchmark:
        spac = benchmark-len(i)
        org = i
        spacstr = spac*" "
        newstr = org+spacstr
        orgindex = sorted_list.index(org)
        sorted_list[orgindex] = newstr
    else:
        pass
    
sorted_worthlist = sorted(numworth_list, key=len, reverse=True)
num_benchmark = len(sorted_worthlist[0])
for i in sorted_worthlist:
    if len(i) <= num_benchmark:
        spac = num_benchmark-len(i)
        org = i
        spacstr = spac*" "
        newstr = org+spacstr
        orgindex = sorted_worthlist.index(org)
        sorted_worthlist[orgindex] = newstr
    else:
        pass
    
print(sorted_list)
print("Name{}Worth".format(benchmark*" "))
print("----{}-----".format(benchmark*" "))
for i in range(10):
    print("{}----{}}".format(sorted_list[i-1],sorted_worthlist[i-1]))
print("Please confirm and check the names above: {}".format(namelist))
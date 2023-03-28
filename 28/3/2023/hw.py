#isdigit

apple = input("pls enter numba: ")

if apple.isdigit():
    print("yas")
else:
    print("no")

#isdigit pt2
    
orange = input("enta la nam: ")

if orange.isdigit():
    print("no")
else:
    print("andrea doing 69")
   
#isalmun

pear = input("enter string of letters and numbas: ")
if pear.isalnum():
    print("a")
else:
    print("gg")

#pls input yr name, 3 stuents from each skool. exercise
xinminlist = []
bowenlist = []
houganglist = []
hougangcounter = 0
xinmincounter = 0
bowencounter = 0
counter=0
tru = True
approvedlist = ["@hougang.edu.sg","@bowen.edu.sg","@xinmin.edu.sg"]
while tru:
    if counter >=9:
        tru = False
    name = input("Please input your name, and school address: "
)
    if xinmincounter >=3:
        approvedlist.remove("@xinmin.edu.sg")
    if bowencounter >=3:
        approvedlist.remove("@bowen.edu.sg")
    if hougangcounter >=3:
        approvedlist.remove("@hougang.edu.sg")

    if name.count("@") == 1:
        oldName = name
        name = name[name.index("@"):]
        if name in approvedlist:
            print("Name is accepted.")
            counter+=1
            if name == "@hougang.edu.sg":
                houganglist.append(oldName)
                hougangcounter+=1
            elif name == "@bowen.edu.sg":
                bowenlist.append(oldName)
                bowencounter+=1
            elif name == "@xinmin.edu.sg":
                xinminlist.append(oldName)
                xinmincounter+=1
        else:
            print("Name is rejected.")
    else:
        print("Name is rejected.")

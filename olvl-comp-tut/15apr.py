def extract_phrases(string):
    strlist = string.split(", ")
    flag = False
    vflag = False
    slist = []
    vowel = "aeiouAEIOU"
    if (strlist[0])[0] == "p" and (strlist[-1])[0]  == "p":
        for i in strlist:
            if i.isalpha():
                flag = True
            else:
                pass
        if flag == True:
            for vowel in strlist:
                for letter in vowel:
                    if letter in vowel:
                        vflag = True
                    else:
                        pass
            if vflag == True:
                return True
def calculate_checksum(list):
    checksum = 0
    for i in list:
        if i%2 == 0:
            checksum+=i
        else:
            checksum-=i
    return checksum

def entry():
    counter=0
    while counter<5:
        
        entry = input("\nplease enter your particulars: ")
        elist = entry.split(", ")
        
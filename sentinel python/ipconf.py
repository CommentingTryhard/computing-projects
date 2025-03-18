
stripad = input("Please inputi n yuor ip address: ")
ipadlist = stripad.split(".")
def ipconf(stripad):
    coloncount = 0
    for i in stripad:
        if i == ".":
            coloncount+=1
            if stripad[i+1] == "0" or stripad[0] == "0":
                return False
            
    if coloncount !=3:
        return False
    for i in ipadlist:
        if int(i) > 255:
            return False
    if len(ipadlist) !=4:
        return False
    
    return True

ipconf(stripad)
def nric(entry):
    def checker(entry):
        if entry[0] == "S":
            if entry[1:7].isdigit():
                if entry[8].isupper():
                    if entry[8].isalpha():
                        print("NRIC ACCEPTED!!!!!!!!")
                        flag = True
                        break
                    else:
                        counter+=1
                        print("FAILURE")
                else:
                    counter+=1
                    print("FAILURE")
            else:
                counter+=1
                print("FAILURE")
        else:
            counter+=1
            print("FAILURE")
    #VARIABLES
    counter = 0
    flag = False

    checker(entry)
    if flag != True:
        print("DEBUG: Counter R{}".format(counter))
        while counter <3:
            entry = input("Please input ur nric again: ")
            checker()
            if flag == True:
                counter+=1000000
            else:
                pass   
nric("S1234567p")
            
    
    
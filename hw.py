def nric(entry):
    def checker():
        if entry[0] == "S":
            if entry[1:7].isdigit():
                if entry[8].isupper():
                    if entry[8].isalpha():
                        print("NRIC ACCEPTED!!!!!!!!")
                        break
                    else:
                        counter+=1
                        print("FAILURE")
                        passe = entry
                else:
                    counter+=1
                    print("FAILURE")
                    passe = entry
            else:
                counter+=1
                print("FAILURE")
                passe = entry
        else:
            counter+=1
            print("FAILURE")
            passe = entry
        
        
    
    
    
    
    
    
    
    
nric("S1234567p")
            
    
    
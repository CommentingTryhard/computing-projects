"""
1. Write a Python function `validate_password` that takes a string as input and validates it to ensure
 it meets the following criteria: 
   - Contains at least one uppercase letter, one lowercase letter, one digit, and one special 
   character (!@#$%^&*).
   - Is at least 10 characters long.
   - Does not contain any spaces.
   If the password does not meet these criteria, prompt the user to enter a valid password until 
   it is provided. The function should return the validated password.
"""

def validate_password(string):
    masterflag = True
    stringflag = True
    def ask_password():
        string = input("Please reenter your password for validation: ")
        return string
    while masterflag:
        upperflag = False
        lowerflag = False
        digitflag = False
        specflag = False

        for i in string:
            if i.isupper():
                upperflag = True
            elif i.islower():
                lowerflag = True
            elif i.isdigit():
                digitflag = True
            elif i in "(!@#$%^&*).":
                specflag = True
            else:
                pass
        if (upperflag == True) and (lowerflag == True) and (digitflag == True) and (specflag == True):
            if len(string)>9:
                for i in string:
                    if i == " ":
                        stringflag = False
                    else:
                        pass
                if stringflag == True:
                    print("Your password is validated.")
                    masterflag = False
                    return(string)
                else:
                    print("Your password contains spaces.")
                    string = ask_password()
                    pass
            else:
                print("Your password is too short.")
                string = ask_password()
                pass
        else:
            print("Your password is lacking the character type requirement.")
            string = ask_password()
            pass
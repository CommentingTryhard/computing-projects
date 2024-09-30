def find_max_min(lst):
    def find_max(lst):
        top = lst[0]
        for i in lst:
            if i>=top:
                top = i
        return top    
    def find_min(lst):
        bottom = lst[0]
        for i in lst:
            if i<=bottom:
                bottom = i
        return bottom
    return find_min(lst) and find_max(lst)

def is_valid_password(password):
    flag = True
    lenspaceflag = False
    letterflag = False
    numberflag = False
    while flag:
        if len(password)>=8:
            for i in password:
                if not(i.isspace()):
                    lenspaceflag = True
        for i in password:
            if i.isdigit():
                numberflag = True
        for i in password:
            if i.isalpha():
                letterflag = True
        if lenspaceflag == True and numberflag == True and letterflag == True:
            flag = False
            return password
        else:
            password = input("Please input your password: ")


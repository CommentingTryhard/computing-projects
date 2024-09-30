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

def lenchecker(str1, str2):
    if len(str1) == len(str2):
        return True
    else:
        return False

def are_anagrams(s1, s2):
    s1list = []
    for i in s1:
        if not(i.isspace()):
            s1list.append(i)
    s2list = []
    for i in s2:
        if not(i.isspace()):
            s2list.append(i)
    s1list = s1list.sort()
    s2list = s2list.sort()
    if s1list == s2list:
        return True
    else:
        return False

def greater_than_ten_or_even(n):
    if n <10:
        if n&2==0:
            return False
        else:
            return True
    else:
        return True


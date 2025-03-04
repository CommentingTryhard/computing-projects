splitlist = []
string = "the cat is very cute" 
def split(sentence):
    lis = sentence.rsplit()
    return lis

def check_list():
    word = input("Please input your word: ")
    lis = split(sentence)
    for i in lis:
        if i == word:
            flag = True
        else:
            flag = False
    if flag == True:
        print("Yes")
    else:
        print("No")
        
def reverse():
    lis = split(sentence)
    for i in lis:
        l = lis[-1]
        if i != l:
            o = lis[0]
            lis.append(o)
            lis.remove(lis[0])
        else:
            break
    ops = "".join(lis)
    return ops
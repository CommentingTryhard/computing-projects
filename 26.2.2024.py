#create an algorithnm to check the number of letter that appear in a setence.
#The letter is requested as input.

#create an algortihn that remove all instances of that word
def lettercounter():
    sentence = input("Please enter ur sentence: ")
    letter = input("Please enter ur letter: ")
    counter = 0
    for i in sentence:
        if letter == i:
            counter+=1
        else: pass
    print(counter)

def letterremover():
    sentence = input("Please enter ur sentence: ")
    letter = input("Please enter ur letter: ")
    print(sentence.replace(letter, ""))

def evenletterreplace():
    sentence = input("Please enter ur sentence: ")
    vowels = "AEIOUaeiou"
    for index, value in enumerate(sentence):
        if value in vowels:
            if index%2==0:
                sentence.replace(value, ":")
                flag = True
            else:
                flag = False
        else:
            flag = False

def splitter():
    senlist = []
    counter = 0
    sentence = input("Please enter ur sentence: ")
    for index, value in enumerate(sentence):
        for i in sentence:
            if i == value:
                counter+=1

def imcrazy():
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    sentence

lists = []
def akai():
    id = input("Enter ur id: ")
    id = id.isupper()
    if id in lists:
        print("Permitted")
    else:
        print("Go suck balls")
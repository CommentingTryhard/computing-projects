#create a function called secondlast(), that is sorted based on ther second last letter
wordlist = []

def secondlast():
    for i in range(5):
        word = input("Please input ur words: ")
        wordlist.append(word)
    
    def lister(o):
        o = o[-2]
        return o
    
    wordlist.sort(key = lister)
    print(wordlist)
        
secondlast()
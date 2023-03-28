wordlist = []
for i in range(3):
    counter = 0
    word = input("Enter word: ")
    for letter in word:
        if letter in "AEIOUaeiou":
            counter +=1
        else:
            pass
    if counter >= 2:
        word = "Big" + word
        wordlist.append(word)
    else:
        word = "Small" + word
        wordlist.append(word)

print(wordlist)  

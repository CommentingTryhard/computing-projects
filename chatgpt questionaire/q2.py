"""
2. Create a Python program `unique_words_counter` that takes a string as input and counts the number 
of unique words in it. Ignore punctuation marks and consider words case-insensitively. Reprompt the 
user if an empty string is provided until a valid input is given.
"""

def unique_words_counter(string):
    string.split(" ")
    for i in string:
        for letters in i:
            if i in "!@#$%^&*()[]<>,.?/:;''\|":
                pass #due for update and redo
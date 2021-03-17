import json
from difflib import get_close_matches

data = json.load(open("data.json"))     
word = input("Please enter a word:")    

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn =  input("Are you looking for '%s'? Y or N " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Can't find this word in data."
        else:
            return "Can't understand your input, please again."
    else: 
        return "Can't find this word in data."

print(translate(word))
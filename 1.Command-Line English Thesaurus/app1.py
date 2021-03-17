import json
from difflib import get_close_matches     #get_close_matches 找寻list中最匹配的项

data = json.load(open("data.json"))     
word = input("Please enter a word:")    

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]                               #上面两种情况为如果这个词只有大写或首字母大写形式：如USA、NATO
    elif len(get_close_matches(word,data.keys())) > 0:          #如果对应的找寻项不为0
        yn =  input("Are you looking for '%s'? Y or N " % get_close_matches(word, data.keys())[0])
        if yn == "Y":                                           
            return data[get_close_matches(word, data.keys())[0]] #对应项的最匹配项 第一个
        elif yn == "N":
            return "Can't find this word in data."              #如果不是这个则回答N==>No
        else:
            return "Can't understand your input, please again."
    else: 
        return "Can't find this word in data."

output = translate(word)

if type(output) == list:                                        #如果输出内容是list，指有输出函数的内容
    for item in output:
        print(item)
else:
    print(output)                                               #如果输出内容不是list，则输出的函数的其他状态
def word_count (split_words):
    split = len(split_words.split())
    return split




def character_count (split_letters):
    dictionary = {}
    lowwer = split_letters.lower()
    for letter in lowwer:
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] = dictionary[letter] + 1
    return dictionary

def myFunc(e):
        return e["num"]

def sort (dic_of_char):
    num = []
    let = []
    for a in dic_of_char.values():
        num.append(a)        
    for b in dic_of_char:
        let.append(b)
    pairs = []    
    for i in range(len(let)):        
        pairs.append({"char":let[i],"num": num[i]})
    
    pairs.sort(reverse=True, key=myFunc)
    return pairs

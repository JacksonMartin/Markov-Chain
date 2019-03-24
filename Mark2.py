import random

def marktable(text, lengths):
    table = {}
    for i in range(len(text)-lengths):
        key = text[i:i+lengths]
        if key in table:
            table[key]= table[key]+1
        else:
            table[key]=1
    return table


def newchar(array, string):
    chance = {}
    total = 0
    for key in array.keys():
        if key[0:len(key)-1] == string:
            chance[key] = array[key]
            total = total + array[key]
    if total == 0:
        return False
    flip = random.randint(1, total)
    for key in chance.keys():
        if chance[key] >= flip:
            return key
        flip = flip-chance[key]

def markov(text, length, order):
    table = marktable(text, order)
    current = text[0:order-1]
    output = current
    i=0
    while i < length-order:
        current = newchar(table, current)
        if current == False:
            return (output)
        current = current[1:len(current)+1]
        output = output+current[len(current)-1]
        i = i+1
    return(output)



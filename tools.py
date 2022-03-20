alphalist = [] #add alphabets in decreasing order of frequency as they appear in the eng language
def replace(ciphertxt,guesses): #guesses is a dict of key=cipher value value=plain value
    ciphlist = list(ciphertxt)
    L = []
    for i in ciphlist:
        if i in guesses.keys():
            L+=guesses[i]
        else:
            L+=i
    res = ''
    for i in L:
        res+=i
    return res

#TODO
def letterfreq(ciphertxt): #will return list of characters sorted by frequency of appearance (decreasing order)
    freq_dict = {} # Dictionary of character corresponding to its frequency
    for i in ciphertxt:
        if i in freq_dict: #if character is already in dictionary, increase frequency by 1
            freq_dict[i] += 1
        else:#if character is not in dictionary, frequency is now 1
            freq_dict[i] = 1
    return freq_dict

print(letterfreq("Alexander, The Great"))



alphalist = [] #add alphabets in decreasing order of frequency as they appear in the eng language
def replace(ciphertxt,guesses): #guesses is a dict of key=cipher value value=plain value
    ciphlist = list(ciphertext)
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
    pass


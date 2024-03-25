alphalist = ["E","T","A","I","N","O","S","H","R","D","L","U","C","M","F","W","Y","G","P","B","V","K","Q","J","X","Z"] #add alphabets in decreasing order of frequency as they appear in the eng language
def replace(ciphertxt,guesses): #guesses is a dict of key=cipher value value=plain value
    res = ""
    for i in ciphertxt:
        if i in guesses.keys():
            res += guesses[i]
        else:
            res += i 
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



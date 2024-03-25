from tools import *
import string

cipher_text = "𐐉𐐏 𐐞𐐅𐐂 𐐀𐐕𐐏𐐡𐐕𐐝 𐐐𐐃 𐐁𐐜𐐂𐐕𐐎𐐝, 𐐘𐐍𐐂𐐏𐐁 𐐞𐐅𐐂 𐐀𐐐𐐍𐐐𐐜𐐝, 𐐤𐐉𐐞𐐅 𐐝𐐞𐐜𐐐𐐌𐐂𐐝 𐐐𐐃 𐐀𐐜𐐂𐐕𐐞𐐉𐐡𐐉𐐞𐐛, 𐐤𐐂 𐐁𐐐 𐐏𐐐𐐞 𐐍𐐐𐐝𐐂. 𐐎𐐠𐐍𐐞𐐉𐐔𐐍𐐛 𐐞𐐅𐐂 𐐉𐐎𐐕𐐄𐐂 𐐘𐐛 𐐃𐐉𐐃𐐞𐐛, 𐐎𐐕𐐌𐐂 𐐉𐐞 𐐄𐐜𐐕𐐏𐐁, 𐐤𐐉𐐞𐐅 𐐂𐐕𐐀𐐅 𐐘𐐜𐐠𐐝𐐅𐐝𐐞𐐜𐐐𐐌𐐂, 𐐍𐐂𐐞 𐐠𐐝 𐐂𐐧𐐔𐐕𐐏𐐁."

freq_dict = letterfreq(cipher_text)

guess_dict = {"𐐉":"I","𐐏":"N","𐐞":"T","𐐅":"H","𐐂":"E"}

# first_decode = replace(cipher_text,guess_dict)
# print(first_decode)

freq_sorted = sorted(freq_dict.items(),key= lambda x:x[1],reverse=True)
# print(freq_sorted)
freq_list = []
for l in freq_sorted:
    l = l[0]
    if not (l == " " or l in string.punctuation):
        freq_list.append(l)

j = 0
for i in range(len(freq_list)):
    l = freq_list[i]
    if l not in guess_dict.keys():
        a = alphalist[j]
        if a not in guess_dict.values():
            j += 1
            guess_dict[l] = a

# second_decode = replace(cipher_text,guess_dict)
# print(second_decode)
guess_dict["𐐤"] = "W"
guess_dict[cipher_text[8]] = "A"
guess_dict["𐐀"] = "C"
guess_dict["𐐐"] = "O"
guess_dict['𐐃'] = "F"
guess_dict["𐐛"] = "Y"
guess_dict["𐐜"] = "R"
guess_dict["𐐡"] = "V"
guess_dict["𐐝"] = "S"
guess_dict["𐐌"] = "K"
guess_dict["𐐁"] = "D"
guess_dict["𐐎"] = "M"
guess_dict["𐐍"] = "L"
guess_dict["𐐘"] = "B"
guess_dict['𐐠'] = "U"
guess_dict["𐐔"] = "P"
guess_dict["𐐄"] = "G"
guess_dict["𐐧"] = "X"
print(alphalist)
print(freq_list)
print(guess_dict)
third_decode = replace(cipher_text,guess_dict)
print(third_decode)
# print("C" in guess_dict.keys())


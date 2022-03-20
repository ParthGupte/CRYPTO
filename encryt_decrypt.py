from modmatrices import *

def vec_encrypt(p,k):
    if isinstance(p,ModMatix) and isinstance(k,ModMatix):
        if p.isvector():
            k.multiply(p)
            return k
        else:
            print("p is not a vector")
    else:
        print("Enter valid ModMatix objects")

def vectoascii(vec):
    if vec.isvector():
        txt = ''
        for row in vec.array:
            i = row[0]
            if i<32:
                txt += chr(126-i)
            else:
                txt += chr(i)
        return txt
    else:
        print("Input should be vector")

def encrypt(p,k):
    base = 127
    n = len(p)
    p_list = []
    if n<=400:
        for i in list(p):
            p_list.append([ord(i)])
        p_list.extend([[ord('~')]]*(400-n))
        p_vec = ModMatix(np.array(p_list),base)
        return vectoascii(vec_encrypt(p_vec,k))
    if n>400:
        t = empty(base)
        while len(p)>0:
            t.vec_concat(encrypt(p[:400],k))
            p = p[400:]
        return vectoascii(t)
    
def decrypt(t,k):
    return encrypt(t,k.inv()).rstrip('~')

##### test







    
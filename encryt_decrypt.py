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

def encrypt(p,k):
    base = 127
    n = len(p)
    p_list = []
    if n<=400:
        for i in list(p):
            p_list.append([ord(i)])
        p_list.extend([[ord('~')]]*(400-n))
        p_vec = ModMatix(np.array(p_list),base)
        return vec_encrypt(p_vec,k)
    if n>400:
        t = empty(base)
        while len(p)>0:
            t.vec_concat(encrypt(p[:400],k))
            p = p[400:]
        return t
    
def decrypt(t,k):
    encrypt(t,k.inv())

##### test







    
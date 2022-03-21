from modmatrices import *

base = 127
chunk_size = 20

def vec_encrypt(p,k):
    if isinstance(p,ModMatix) and isinstance(k,ModMatix):
        if p.isvector():
            k.multiply(p)
            k.value()
            return k
        else:
            print("p is not a vector")
    else:
        print("Enter valid ModMatix objects")

def vectoascii(vec):
    if vec.isvector():
        txt = ''
        for row in vec.array:
            i = int(row[0])
            if i<32:
                txt += chr(161+i)
            else:
                txt += chr(i)
        return txt
    else:
        print("Input should be vector")

def encrypt(p,k):
    n = len(p)
    p_list = []
    if n<=chunk_size:
        for i in list(p):
            p_list.append(ord(i))
        p_list.extend([198]*(chunk_size-n))
        print(p_list)
        p_vec = ModMatix(np.array([p_list]).T,base)
        return vectoascii(vec_encrypt(p_vec,k))
    if n>chunk_size:
        t = empty(base)
        while len(p)>0:
            t.vec_concat(encrypt(p[:chunk_size],k))
            p = p[chunk_size:]
        return vectoascii(t)
    
def decrypt(t,k):
    k.inv()
    return encrypt(t,k).rstrip(chr(198))

##### test

karr = np.identity(20)
k = ModMatix(karr,base)
t = encrypt("I am a disco dancer.",k)
print(t)
print(decrypt(t,k))






    

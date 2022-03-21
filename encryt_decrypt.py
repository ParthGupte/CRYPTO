from modmatrices import *
import inverse
base = 127
chunk_size = 19

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
    for i in p:
        p_list.append(ord(i))
    p_list.extend([126]*(361-n))
    parr_list = []
    while len(p_list)>0:
        p_chunk = p_list[:chunk_size]
        parr_list.append(p_chunk)
        del p_list[:chunk_size]
    p_arr = np.array(parr_list).T
    P = ModMatix(p_arr,base)
    K = ModMatix(k,base)
    K.multiply(P)
    T = K.array
    t = T.T
    cypher = ''
    for i in range(t.shape[0]):
        t_vec = ModMatix(np.array([t[i]]).T,base)
        cypher += vectoascii(t_vec)
    return cypher


    # if n<=chunk_size:
    #     for i in list(p):
    #         p_list.append(ord(i))
    #     p_list.extend([126]*(chunk_size-n))
    #     print(p_list)
    #     p_vec = ModMatix(np.array([p_list]).T,base)
    #     return vectoascii(vec_encrypt(p_vec,ModMatix(k,base)))
    # if n>chunk_size:
    #     t = empty(base)
    #     while len(p)>0:
    #         t.vec_concat(encrypt(p[:chunk_size],ModMatix(k,base)))
    #         p = p[chunk_size:]
    #     return vectoascii(t)
    
def decrypt(t,k):
    return encrypt(t,inverse.mod_inverse(k)).rstrip(chr(126))

##### test

karr = np.array(np.identity(chunk_size,dtype='int64'))
k = karr
t = encrypt("I am a disco dancer.",k)
print(t)
print(decrypt(t,k))

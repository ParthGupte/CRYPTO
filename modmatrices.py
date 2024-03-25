import numpy as np
import copy
import inverse
# Every opereration on a ModeMatix object changes the value of the array associated with it and does not create a new object
# So M1.add(M2) will add M1 and M2 and assign the value to M1 similarly for all other operations
# you can import this class into another file by using "from modematrices import *" and then use it the same way in that file as I have here 
def empty(base):
    return ModMatix(np.array([[]]),base).T

class ModMatix:
    def __init__(self, array, base) -> None:
        if len(array.shape) == 2:
            self.base = base
            self.array = np.array(array%self.base,dtype='int64')
            
        else:
            print("Use an 2darray")
    
    def value(self):
        print(self.array,self.base)
    
    def vec_dim(self):
        if self.isvector():
            return self.array.shape[0]
        else:
            print("This is not a vector")

    def add(self,M):
        if isinstance(M,ModMatix):
            if M.base == self.base:
                if M.array.shape == self.array.shape:
                    self.array = (self.array+M.array)%self.base
                else:
                    print("Matrices have different shapes, can't be added")
            else:
                print("Matrices don't have the same base, can't be added")
        else:
            print("Object is not an instance of ModMatrix, can't be added")
    
    def scale(self,mult):
        self.array = (self.array*mult)%self.base
    
    def multiply(self,M):
        if isinstance(M,ModMatix):
            if M.base == self.base:
                if self.array.shape[1] == M.array.shape[0]:
                    prod = np.zeros((self.array.shape[0],M.array.shape[1]))
                    for i in range(prod.shape[0]):
                        for j in range(prod.shape[1]):
                            for k in range(self.array.shape[1]) :
                                prod[i,j] = ( prod[i,j] + (self.array[i,k]*M.array[k,j]) ) % self.base
                    self.array = prod
                else:
                    print("These matices don't have compatible shape for multiplication")
            else:
                print("Matrices don't have the same base, can't be multiplied")
        else:
            print("Object is not an instance of ModMatrix, can't be multiplied")
    
    def inv(self):
        print(self.array)
        invarr = inverse.mod_inverse(np.array(self.array,dtype='int64'))
        print(invarr)
        self.array = np.array(invarr,dtype='int64')
        
    def div(self,M):  # A.div(B) is A times B inverse 
        M_ = M
        M.inv()
        self.multiply(M)
        M = M_

    def isvector(self):
        if isinstance(self,ModMatix):
            return self.array.shape[1] == 1
        else:
            return False
    
    def vec_concat(self,a):
        if a.isvector() and self.isvector():
            self.array = np.concatenate((self.array,a), axis=0)
        else:
            print("Must be a vector")
    
    #def det(self):
    # I will send code for determinant also — Pranjal
        



### test
# m1 = np.array([[1,2,3],[3,2,1],[2,3,1]])
# M1 = ModMatix(m1,2)
# m2 = np.array([[0,1,1],[2,1,1],[0,0,0]])
# M2 = ModMatix(m2,2)
# M1.value()
# M2.value()
# M1.add(M2)
# M1.value
# M1.scale(2)
# M1.value()
# M1.multiply(M2)
# M1.value()
# M1.add(M2)
# M1.value()
# M1.inv()
# M1.value()
# M1.div(M2)
# M1.value()

                
m = np.array([[2,6,1],[11,2,0],[4,1,3]])
M = ModMatix(m,9539)
M.inv()
r = np.array([[3030],[6892],[8773]])
R = ModMatix(r,9539)
M.multiply(R)
print(M.array)



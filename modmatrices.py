import numpy as np
import pandas as pd
import inverse
# Every opereration on a ModeMatix object changes the value of the array associated with it and does not create a new object
# So M1.add(M2) will add M1 and M2 and assign the value to M1 similarly for all other operations
# you can import this class into another file by using "from modematrices import *" and then use it the same way in that file as I have here 
class ModMatix:
    def __init__(self, array, base) -> None:
        if len(array.shape) == 2:
            self.base = base
            self.array = array%self.base
            
        else:
            print("Use an 2darray")
    
    def value(self):
        print(self.array,self.base)
    
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
                            prod[i,j] = sum(self.array[i]*M.array[:,j])
                    self.array = prod%self.base
                else:
                    print("These matices don't have compatible shape for multiplication")
            else:
                print("Matrices don't have the same base, can't be multiplied")
        else:
            print("Object is not an instance of ModMatrix, can't be multiplied")
    
    def inv(self):
        invarr = inverse.mod_inverse(self.array)
        self.array = invarr
    
    def div(self,M):  # A.div(B) is A times B inverse 
        self.multiply(M.inv()) 
    
    def isvector(self):
        return self.array.shape[1] == 0
    
    #def det(self):
    # I will send code for determinant also — Pranjal
        



### test
m1 = np.array([[1,2,3],[3,2,1],[2,3,1]])
M1 = ModMatix(m1,2)
m2 = np.array([[0,1,1],[2,1,1],[0,0,0]])
M2 = ModMatix(m2,2)
M1.value()
M2.value()
M1.add(M2)
M1.value
M1.scale(2)
M1.value()
M1.multiply(M2)
M1.value()
M1.add(M2)
M1.value()
M1.inv()
M1.value()
M1.div(M2)
M1.value()

                
                




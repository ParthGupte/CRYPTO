import numpy as np
import copy

##########################################################################################################################

def row_op(matrices , rows , coeffs) : # Takes a list of matrices (matrices), row indices (rows) and coefficients (coeffs)
                                       # len(rows) = len(coeffs) + 1
                                       # Suppose rows = [r0 , r1 , ... , rn], coeffs  = [c1 , ... , cn]
                                       # Then, r1 --> r1 + c1*r0 , r2 --> r2 + c2 * r0 , ... , rn --> rn + cn * r0

    for M in matrices :
        for r in range(len(coeffs)) :
            M[rows[r+1]] += coeffs[r]*M[rows[0]]


def reducer(M,I,a) : # Takes matrices M and I and some a = 0 , ... , n-1
                     # Makes M[i,a] = 0 for all i = a+1 , ... , n-1 by subtracting required multiple of M[a] from M[i] (this only works if M[a,a] != 0)
                     # If M[a,a] == 0, then it is first made non-zero by adding some other row to M[a] and then the aforementioned subtraction is done
                     # All row operations done in M are also done in I (row_op() allows us to do row operations on M and I together)
    n = len(M)

    if M[a,a] and a<n-1 : # M[a,a] != 0 part
        row_op( [M,I] , [i for i in range(a,n)] , [-M[i,a]/M[a,a] for i in range(a+1,n)] )

    elif M[a,a] == 0 : # M[a,a] = 0 part

        for i in range(a+1,n) : 

            if M[i,a] != 0 : # Find some row M[i] (i>a) with M[i,a] != 0. The reason for i>a is explained by the usage of reducer() in inverse()
                row_op([M,I] , [i,a] , [1]) # Add this row to M[a]
                reducer(M,I,a) # Then do what was done in the M[a,a] != 0 case
                break

        else : # Refer to usage of reducer() in inverse()
            print("inverse error: Matrix not invertible")
            return -1


def inverse(M) : # Returns the inverse of M, prints "inverse error: Matrix not invertible" and returns None otherwise
                 # Gaussian row elimination algorithm used
    n = len(M)
    A = np.array([[M[i,j] for j in range(n)] for i in range(n)] , dtype = 'float64')
    I = np.identity(n , dtype = 'float64')

    # Step-by-step, we will turn A into the identity matrix and I into the inverse of A using row operations
    
    for i in range(n) : # Loop for finding rref(A)

        if reducer(A,I,i) == -1 : # M is not invertible in this case
            return None

        else : # Make all diagonal entries of A into 1
            I[i] = I[i]/A[i,i]
            A[i] = A[i]/A[i,i]
     
    # A is now in row-reduced echelon form

    for i in range(n-1 , 0 , -1) : # Use diagonal elements of A to make A into the identity
                                   # We need not edit A anymore; there is no point in doing so. Instead, we only do those row operations in I which (contd)
                                   # (contd) we would have done to make A into the identity
        for j in range(i) :
            I[j] = I[j] - A[j,i]*I[i]

    return I

########################################################################################################################
    
q = 131 # We now use the fact that Z_q is a field (since q is a prime)


def mod_inv(x) : # Returns the mod q multiplicative inverse of x
    if x%q==0 :
        print("mod_inv error; division by 0")

    else :
        y = 1
        for i in range(q-2) : # The multiplicative inverse of x mod q is x^(q-2) (Fermat's Little Theorem)
            y = (y*x)%q

        return y


def mod_reducer(M,I,a) : # Same as reducer(), but division is replaced by modular division
    n = len(M)

    if M[a,a]%q and a<n-1 :
        row_op( [M,I] , [i for i in range(a,n)] , [ ( -M[i,a] * mod_inv(M[a,a]) ) % q for i in range(a+1,n)] )

    elif M[a,a]%q == 0 :

        for i in range(a+1,n) :

            if M[i,a]%q != 0 :
                row_op([M,I] , [i,a] , [1])
                mod_reducer(M,I,a)
                break

        else :
            print("mod_inverse error: Matrix not invertible")
            return -1


def mod_inverse(M) : # Returns the modular multiplicative inverse of M. Same algorithm as inverse() but with division replaced by modular division
    n = len(M)
    A = copy.deepcopy(M)
    I = np.array([[1 - np.sign((i-j)**2) for i in range(n)] for j in range(n)] , dtype = 'int') # I is the identity matrix
    
    for i in range(n) :

        if mod_reducer(A,I,i) == -1 :
            return None

        else :
            I[i] = ( I[i] * mod_inv(A[i,i]) ) % q
            A[i] = ( A[i] * mod_inv(A[i,i]) ) % q
    
    for i in range(n-1 , 0 , -1) :
        for j in range(i) :
            I[j] = I[j] - A[j,i]*I[i]

    return np.matrix([[I[i,j]%q for i in range(n)] for j in range(n)])

#author: Martin Ægidius, DTU, 2022


def matrix_mult(A,B):
    n = len(A) #size solely used for preallocation for output n x n 
    C = [ [ 0 for i in range(n) ] for j in range(n) ] #preallocate for efficiency
    for i in range(len(A)): #rows of A
        for j in range(len(B[0])): #columns of B
            for k in range(len(B)): #rows of B
                C[i][j] += A[i][k] * B[k][j] #result of C
    return C
    
# 3x3 matrix example
A = [[12,7,3],
    [4,5,6],
    [7,8,9]]
B = [[5,8,1],
    [6,7,3],
    [4,5,9]]

C = matrix_mult(A,B) #create resultant
for r in C:
    print(r)
    

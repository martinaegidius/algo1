
A = [1,2,3,4,2,3,3,3,2,1,1,1,1,0]

holder_array = [None]

[(x[1]-(x[0])) for x in zip(A,A[1:]+[0])]
print(A)

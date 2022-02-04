def f(A,n):
    if (n==0):
        return 0
    else:
        return f(A,n-1)+A[n-1]
    
def f2(A,n):
    seqsum = 0.0
    for i in range(n):
        seqsum += A[n-1]
    return seqsum

A = [3,3,3]
n = len(A)
out = f(A,n)

out2 = f2(A,n)
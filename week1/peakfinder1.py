

n = int(input())

A = list(map(int,input().split()))

def peak1(A,n):
    if A[0] >= A[1]: 
        return 0
    for i in range(1,n-2):
        if (A[i-1] <= A[i] and A[i] >= A[i+1]):
            return i
    if A[n-2]<=A[n-1]:
        return n-1
        
print(peak1(A,n))


#A = [1,3,7,15,11,2,3,6,8,6]
#outer = peak1(A,len(A))
#print(outer)
        
        

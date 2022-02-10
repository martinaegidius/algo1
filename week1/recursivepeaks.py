n = int(input())
A = list(map(int,input().split()))
#A = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
#A = [1, 3, 7, 15, 17, 11, 2, 3, 6, 8, 7, 5, 9, 5, 23]
#n = len(A)

def peak3(A,i,j):
    m = (i+j)//2
    if m <= 0 and A[m] >= A[m+1]:
        return m
    if m >= j and A[m]>=A[m-1]:
        return m
    if (A[m]>=A[m-1] and A[m]>=A[m+1]): 
        return m
    elif A[m-1] >= A[m]:
        return peak3(A,i,m-1)
    elif A[m]<=A[m+1]:
        return peak3(A,m+1,j)
            
print(peak3(A,0,n-1))



        
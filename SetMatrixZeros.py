#Set MAtrix Zeros

for _ in range(int(input())):
    n=int(input())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split())))
    rF=False
    cF=False
    for i in range(0,n) : 
        for j in range(0, len(A[0])): 
            if (i == 0 and A[i][j] == 0) : 
                rF = True   
            if (j == 0 and A[i][j] == 0) : 
                cF = True
            if (A[i][j] == 0) : 
                A[0][j] = 0
                A[i][0] = 0
    for i in range(1,n) : 
        for j in range(1, len(A[0])): 
            if (A[0][j] == 0 or A[i][0] == 0) : 
                A[i][j] = 0
    if rF:
        A[0][:]=[0]*len(A[0])
    if cF:
        for i in range(n):
            A[i][0]=0
    for i in A:
        print(*i)
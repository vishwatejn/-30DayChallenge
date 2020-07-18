#Rotate by 90 degrees ANTI -clockwise
import numpy as np
for _ in range(int(input())):
    n=int(input())
    B=list(map(int,input().split()))
    A=[]
    for i in range(n):
        A.append(B[n*i:n*i+n])
    A=np.array(A)
    A=np.transpose(A)
    A=A[::-1]
    for i in A:
        print(*i,end=" ")
    print()

#Rotate by 90 degrees Clockwise
#code
import numpy as np
for _ in range(int(input())):
    n=int(input())
    B=list(map(int,input().split()))
    A=[]
    for i in range(n):
        A.append(B[n*i:n*i+n])
    A=np.array(A)
    A=np.transpose(A)
    #A=A[::-1]
    for i in A:
        print(*i[::-1],end=" ")
    print()
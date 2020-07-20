# 2 Sum Problem
for _ in range(int(input())):
    n,total=map(int,input().split())
    a=list(map(int,input().split()))
    d=dict()
    for i in range(n):
        d[a[i]]=i
    for i in range(n):
        if total-a[i]!=a[i] and total-a[i] in d:
            print(i,d[total-a[i]])
    
#code
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    tot=(n*(n+1))//2
    c=0
    s=0
    for i in range(n):
        if a[i]<=k:
            c+=1
        else:
            s+=(c*(c+1))//2
            c=0
    s+=(c*(c+1))//2
    ans=tot-s
    '''
    for i in range(n):
        for j in range(i,n):
            if max(a[i:j+1])>k:
                ans+=1
    '''
    print(ans)
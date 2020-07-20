for _ in range(int(input())):
    n,total=map(int,input().split())
    a=list(map(int,input().split()))
    d=dict()
    for i in range(n-1):
        for j in range(i+1,n):
            d[a[i]+a[j]]=[i,j]
    ans=[]
    for i in range(n-1):
        for j in range(i+1,n):
            s=a[i]+a[j]
            if total-s in d:
                xy=d[total-s]
                if i and j not in xy:
                    ans.append(sorted[i,j,xy[0],x[1]]) 
    print(ans)
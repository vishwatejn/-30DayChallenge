for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    ans=0
    while i<n:
        j=i
        while j+1<n and a[j+1]>a[j]:
            j+=1
        x=j-i+1
        ans+=(x*(x+1))//2-x
        if i==j:
            i+=1
        else:
            i=j
    print(ans)
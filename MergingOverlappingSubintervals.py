#Merging Overlapping Sub-intervals

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    times=[]
    for i in range(n):
        times.append([a[2*i],a[2*i+1]])
    times.sort()
    ans=[times[0]]
    for i in range(1,n):
        if times[i][0]<=ans[-1][1]:
            ans[-1][1]=max(ans[-1][1],times[i][1])
        else:
            ans.append(times[i])
    for i in ans:
        print(*i,end=" ")
    print()
            
    
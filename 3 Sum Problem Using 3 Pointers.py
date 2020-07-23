# 3 Sum Problem Using 3 Pointers
for _ in range(int(input())):
    n, tot = map(int, input().split())
    a = [int(i) for i in input().split()]
    if n < 3:
        print(0)
    else:
        i = 0
        j = 1
        k = n-1
        f = 0
        while i < k:
            if j >= k:
                i += 1
                j = i+1
                k = n-1
            if a[i]+a[k] >= tot:
                k -= 1
            elif a[i]+a[k] < tot:
                if a[i]+a[j]+a[k] == tot:
                    f = 1
                    print(1)
                    break
                elif a[i]+a[j]+a[k] > tot:
                    k -= 1
                else:
                    j += 1
        if f == 0:
            print(0)
    '''
    O(n^2)
    d=dict()
    for i in range(n):
        for j in range(i+1,n):
            d[a[i]+a[j]]=[i,j]
    f=0
    for i in range(n):
        if tot-a[i] in d and i!=d[tot-a[i]][0] and i!=d[tot-a[i]][1]:
            print(1)
            f=1
            brea
    if f==0:
        print(0)
    '''

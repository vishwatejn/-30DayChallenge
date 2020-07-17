#Merge 2 sorted arrays without extra space

def nextGap(gap): 
    if (gap <= 1): 
        return 0
    return (gap // 2) + (gap % 2)
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    '''
    #Method 3
    gap = n + m 
    gap = nextGap(gap) 
    while gap > 0 :  
        i = 0
        while i + gap < n : 
            if (a[i] > a[i + gap]): 
                a[i],a[i + gap] = a[i + gap], a[i] 
            i += 1
        j = gap - n if gap > n else 0
        while i < n and j < m: 
            if (a[i] > b[j]): 
                a[i], b[j] = b[j],a[i] 
            i += 1
            j += 1
        if (j < m):  
            j = 0
            while j + gap < m : 
                if (b[j] > b[j + gap]): 
                    b[j],b[j + gap] = b[j + gap],b[j] 
                j += 1
        gap = nextGap(gap)
    a=a+b
    print(*a)
    '''
    '''
    #Method 2
    a=a+b
    a.sort()
    print(*a)
    '''
    '''
    #Method 1
    for i in range(n-1, -1, -1):
        last = a[m-1] 
        j=m-2
        while(j >= 0 and a[j] > b[i]): 
            a[j+1] = a[j] 
            j-=1
        if (j != m-2 or last >b[i]): 
            a[j+1] = b[i] 
            b[i] = last 
    print(*a,end=" ")
    print(*b)
    '''
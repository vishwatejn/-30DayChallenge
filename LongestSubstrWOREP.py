for _ in range(int(input())):
    s=input()
    n=len(s)
    lastInd=[-1]*256
    res=0
    i=0
    for j in range(n):
        i=max(i,lastInd[ord(s[j])]+1)
        res=max(res,j-i+1)
        lastInd[ord(s[j])]=j
    print(res)
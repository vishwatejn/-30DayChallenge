# Excel Column Name
for _ in range(int(input())):
    n=int(input())
    op=""
    m=[]
    while n>26:
        if n%26==0:
            m.append(26)
            n=n//26-1
        else:
            m.append(n%26)
            n=n//26
    op+=chr(64+n)
    x=len(m)
    for j in range(x-1,-1,-1):
        op+=chr(64+m[j])
    print(op)

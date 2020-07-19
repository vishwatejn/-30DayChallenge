# Count trailing zeros in factorial of a number
for _ in range(int(input())):
    n=int(input())
    i=5
    ans=0
    while (n/i>=1):
        ans+=int(n/i)
        i=i*5
    print(ans)
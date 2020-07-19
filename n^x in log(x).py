# n^x in log(x)
def power(n,x):
    ans=1
    while (x > 0): 
        if (x%2==1) : 
            ans = ans*n   
        x= x >> 1
        n = n * n      
    return ans

for _ in range(int(input())):
    n,x=map(int,input().split())
    print(power(n,x))
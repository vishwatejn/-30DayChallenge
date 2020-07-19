# No.of Paths in a Grid

from math import factorial
M=10**9+7
for _ in range(int(input())):
    n,m=map(int,input().split())
    print((factorial(m+n-2)//(factorial(n-1)*factorial(m-1)))%M)
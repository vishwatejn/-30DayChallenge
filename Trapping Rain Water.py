# Trapping Rain Water
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    l = [0]*n
    r = [0]*n
    l[0] = a[0]
    for i in range(1, n):
        l[i] = max(l[i-1], a[i])
    r[-1] = a[-1]
    for i in range(n-2, -1, -1):
        r[i] = max(r[i+1], a[i])
    ans = 0
    for i in range(n):
        ans += min(l[i], r[i])-a[i]
    print(ans)

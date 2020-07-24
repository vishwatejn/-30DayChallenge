# Minimum Platforms
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    ans = 1
    i = 1
    j = 0
    plat = 1
    while i < n and j < n:
        if a[i] <= b[j]:
            plat += 1
            i += 1
        elif a[i] > b[j]:
            plat -= 1
            j += 1
        ans = max(ans, plat)
    print(ans)

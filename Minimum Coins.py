# Minimum Coins
den = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
for _ in range(int(input())):
    n = int(input())
    j = 9
    ans = []
    while n > 0:
        if n >= den[j]:
            n -= den[j]
            ans.append(den[j])
        else:
            j -= 1
    print(*ans)

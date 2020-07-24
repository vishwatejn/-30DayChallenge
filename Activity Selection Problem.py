# Activity Selection Problem
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = []
    for i in range(n):
        c.append([a[i], b[i], i+1])
    c.sort(key=lambda x: x[1])
    ans = [c[0]]
    # print(c)
    for i in range(1, n):
        if c[i][0] >= ans[-1][1]:
            ans.append(c[i])
    print(len(ans))

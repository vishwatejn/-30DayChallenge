# Fractional Knapsack
for _ in range(int(input())):
    n, w = map(int, input().split())
    a = [int(i) for i in input().split()]
    vals = []
    for i in range(0, 2*n, 2):
        vals.append([a[i], a[i+1]])
    vals.sort(key=lambda x: (x[0]/x[1]))
    vals = vals[::-1]
    ans = 0
    i = 0

    while w > 0 and i < n:
        if vals[i][1] <= w:
            w -= vals[i][1]
            ans += vals[i][0]
            i += 1
        else:
            ans += vals[i][0]*(w/vals[i][1])
            w = 0
            i += 1
    print(round(float(ans), 2))

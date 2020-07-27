# Next Greatest element
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = []
    stack = []
    for i in range(n-1, -1, -1):
        if len(stack) == 0:
            ans.append(-1)
            stack = stack+[a[i]]
        else:
            while len(stack) > 0 and stack[0] <= a[i]:
                stack = stack[1:]
            if len(stack) == 0:
                ans.append(-1)
                stack = stack+[a[i]]
            else:
                ans.append(stack[0])
                stack = [a[i]]+stack
    ans = ans[::-1]
    print(*ans)

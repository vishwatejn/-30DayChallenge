# Longest Palindromic Substring
for _ in range(int(input())):
    a = input()
    n = len(a)
    ans = ""
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[i:j+1] == a[i:j+1][::-1] and len(a[i:j+1]) > len(ans):
                ans = a[i:j+1]
    if len(ans) > 0:
        print(ans)
    else:
        print(a[0])

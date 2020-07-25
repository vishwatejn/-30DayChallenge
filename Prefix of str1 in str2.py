# Prefix of str1 in str2
for _ in range(int(input())):
    a = input()
    b = input()
    n = len(a)
    i = 0
    ans = -1
    while i < n:
        try:
            ans = b.index(a[:i+1])
        except:
            print(ans, a[:i])
            break
        i += 1

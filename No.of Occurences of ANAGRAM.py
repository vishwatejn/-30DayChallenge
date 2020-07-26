# No.of Occurences of ANAGRAM
def dic(a):
    d = dict()
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


for _ in range(int(input())):
    s = input()
    c = input()
    a = len(c)
    d = dict()
    for i in c:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    i = 0
    ans = 0
    while i < len(s)-a+1:
        if d == dic(s[i:i+a]):
            # print(s[i:i+a])
            ans += 1
        i += 1
    print(ans)

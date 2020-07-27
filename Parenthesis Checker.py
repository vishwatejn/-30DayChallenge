# Parenthesis Checker
a = ["{", "}", "(", ")", "[", "]"]
for _ in range(int(input())):
    s = input()
    ac = 0
    bc = 0
    cc = 0
    n = len(s)
    flag = True
    for i in range(n):
        if s[i] == a[0]:
            ac += 1
        if s[i] == a[2]:
            bc += 1
        if s[i] == a[4]:
            cc += 1
        if s[i] == a[1]:
            if ac == 0:
                flag = False
                break
            else:
                ac -= 1
        if s[i] == a[3]:
            if bc == 0:
                flag = False
                break
            else:
                bc -= 1
        if s[i] == a[5]:
            if cc == 0:
                flag = False
                break
            else:
                cc -= 1
    if ac > 0 or bc > 0 or cc > 0:
        flag = False
    if flag:
        print("balanced")
    else:
        print("not balanced")

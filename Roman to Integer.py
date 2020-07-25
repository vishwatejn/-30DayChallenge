# Roman to Integer
vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for _ in range(int(input())):
    s = input()
    a = vals[s[-1]]
    for i in range(len(s)-1):
        x = vals[s[i]]
        y = vals[s[i+1]]
        if(x >= y):
            a += x
        else:
            a -= x
    print(a)

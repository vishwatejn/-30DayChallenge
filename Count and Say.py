# Count and Say
a = ["1"]
for i in range(1, 21):
    x = a[i-1]
    i = 0
    op = ""
    while i < len(x):
        c = 1
        y = x[i]
        j = i+1
        while j < len(x) and x[j] == x[i]:
            c += 1
            j += 1
        op += str(c)+y
        i = j
    a.append(op)
# print(a)
for _ in range(int(input())):
    print(a[int(input())-1])

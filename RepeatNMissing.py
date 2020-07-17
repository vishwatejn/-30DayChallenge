#Repeat and Missing Number

for _ in range(int(input())):
    n=int(input())
    ar=input().split()
    for i in range(n):
        if int(ar[abs(int(ar[i]))-1])>0:
            ar[abs(int(ar[i]))-1]=-int(ar[abs(int(ar[i]))-1])
        else:
            print(abs(int(ar[i])),end=" ")
    #print(ar)
    for i in range(n):
        if int(ar[i])>0:
            print(i+1)
            break
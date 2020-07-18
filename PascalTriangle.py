#Pascal Triangle row
for _ in range(int(input())):
    n=int(input())
    C=1
    for i in range(1,n+1):
        print(C, end = " ");  
        C = int(C * (n - i)/ i)
    print()
#Triangle upto n rows
for _ in range(int(input())):
    n=int(input())
    for l in range(1,n+1):
        C=1
        for i in range(1,l+1):
            print(C, end = " ");  
            C = int(C * (l - i)/ i)
        print()
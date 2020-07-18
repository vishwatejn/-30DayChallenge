#Stock buy ,sell
def stock(price, n): 
    buy=[]
    sell=[]
    if (n == 1): 
        return buy,sell
    i = 0
    while (i < n - 1): 
        while ((i <n-1) and (price[i + 1] <= price[i])): 
            i += 1
        if (i == n - 1): 
            break
        buy.append(i) 
        i += 1
        while ((i < n) and (price[i] >= price[i - 1])): 
            i += 1
        sell.append(i - 1)
    return buy,sell
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y=stock(a,n)
    if len(x)==0 or len(y)==0:
        print("No Profit")
    else:
        for i in range(len(x)):
            print("("+str(x[i])+" "+str(y[i])+")",end=" ")
        print()
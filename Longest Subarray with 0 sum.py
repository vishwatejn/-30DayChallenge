def maxLen(n, arr):
    #Code here
    d=dict()
    maxi=0
    cursum=0
    for i in range(n):
        cursum+=arr[i]
        if arr[i]==0 and maxi==0:
            maxi=1
        if cursum==0:
            maxi=i+1
        if cursum in d:
            maxi=max(maxi,i-d[cursum])
        else:
            d[cursum]=i
    return maxi
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))

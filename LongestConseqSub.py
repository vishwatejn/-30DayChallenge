def findLongestConseqSubseq(arr, n):
    # code here
    s=set(arr)
    ans=0
    for i in range(n):
        if arr[i]-1 not in s:
            j=arr[i]
            while j in s:
                j+=1
            ans=max(ans,j-arr[i])
    return ans

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(findLongestConseqSubseq(a,n))
#Find the duplicate in an array of N integers

from collections import Counter
def duplicates(arr, n): 
    a=Counter(arr)
    ans=[]
    for i in a:
        if a[i]>1:
            ans.append(i)
    ans.sort()
    if len(ans)>0:
        return ans
    else:
        return [-1]
#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()

# } Driver Code Ends
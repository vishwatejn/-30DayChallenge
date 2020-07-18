# Next Permutation
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in reversed(range(1, n)):
        if arr[i] > arr[i-1]:
            break
    for index in reversed(range(i, n)):
        if arr[index] > arr[i-1]:
            break
    ans =arr[:i-1]
    ans.append(arr[index])
    ans = ans + list(reversed(arr[index+1:]))
    ans.append(arr[i-1])
    ans =ans+ list(reversed(arr[i:index]))
    print(*ans)
            

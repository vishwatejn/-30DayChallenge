# remove Deuplicates in Sorted Array

def remove_duplicate(n, arr):
    j = 0
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[-1]
    j += 1
    return j
    '''
    arr[:]=sorted(set(arr)) 
    return len(arr)
    '''


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = remove_duplicate(n, arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()

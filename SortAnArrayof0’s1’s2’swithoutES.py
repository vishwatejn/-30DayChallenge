#Sort an array of 0’s 1’s 2’s without using extra space or sorting algo

def sort012( a):
    n=len(a)
    low = 0
    high = n- 1
    mid = 0
    while mid <= high: 
        if a[mid] == 0: 
            a[low], a[mid] = a[mid], a[low] 
            low = low + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[high] = a[high], a[mid]  
            high = high - 1
    return a 
for _ in range(int(input())):
    a=list(map(int,input().split()))
    print(*sort012(a))
# Anagrams or not
from collections import Counter
for _ in range(int(input())):
    a, b = input().split()
    if Counter(a) == Counter(b):
        print("YES")
    else:
        print("NO")

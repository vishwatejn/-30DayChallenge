# A to I
def atoi(string):
    try:
        return int(string)
    except:
        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(atoi(string))

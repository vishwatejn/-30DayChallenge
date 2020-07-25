# Integer to Roman

a = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
b = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
a = a[::-1]
b = b[::-1]


def convertRoman(n):
    op = ""
    for i in range(len(a)):
        while n >= b[i]:
            n -= b[i]
            op += a[i]
    return op


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))

# Reverse words of a string
import atexit
import sys
import io


def reverseWords(s):
    # code here
    a = list(s.split("."))
    a = a[::-1]
    op = ""
    print(".".join(i for i in a), end="")


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        s = reverseWords(s)
        print()

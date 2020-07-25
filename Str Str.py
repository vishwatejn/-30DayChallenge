# Str Str
import atexit
import sys
import io


def strstr(s, p):
    # code here
    try:
        return s.index(p)
    except:
        return -1


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        s, p = input().strip().split()
        print(strstr(s, p))

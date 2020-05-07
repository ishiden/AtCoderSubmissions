import sys
import math

input = sys.stdin.readline

def main():
    _is_found = False
    n = int(input())
    for x in range(n+1):
        if math.floor(x * 1.08) == n:
            print(x)
            _is_found = True
            break
    if not _is_found:
        print(':(')

if __name__ == '__main__':
    main()
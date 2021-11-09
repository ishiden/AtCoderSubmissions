import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    X, Y = map(int, input().split('.'))
    ans = str(X)
    if Y >= 7:
        ans += '+'
    elif Y <= 2:
        ans += '-'
    print(ans)

if __name__ == '__main__':
    main()
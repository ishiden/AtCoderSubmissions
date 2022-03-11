import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    for i in range(2):
        if A > B:
            ans += A
            A -= 1
        else:
            ans += B
            B -= 1
    print(ans)

if __name__ == '__main__':
    main()
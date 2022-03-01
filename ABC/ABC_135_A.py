import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'IMPOSSIBLE'
    A, B = map(int, input().split())
    if (A+B)%2 == 0:
        ans = (A+B)//2
    print(ans)

if __name__ == '__main__':
    main()
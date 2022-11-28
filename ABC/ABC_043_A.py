import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    ans = (1 + N)*(N//2)
    if N%2 != 0:
        ans += (1+N)//2
    print(ans)

if __name__ == '__main__':
    main()
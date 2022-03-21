import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    X = int(input())
    if X in [7, 5, 3]:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()
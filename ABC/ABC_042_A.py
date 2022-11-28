import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    s = list(map(int, input().split()))
    s.sort()
    if s[0] == 5 and s[1] == 5 and s[2] == 7:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()
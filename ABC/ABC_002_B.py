import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    W = input().rstrip('\n')
    ans = ''
    boin = set(['a', 'i', 'u', 'e', 'o'])
    for w in W:
        if w in boin:
            continue
        ans += w

    print(ans)

if __name__ == '__main__':
    main()
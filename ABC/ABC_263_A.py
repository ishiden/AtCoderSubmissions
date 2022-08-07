import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    cards = list(map(int, input().split()))
    cards.sort()
    d = collections.defaultdict(int)
    for c in cards:
        d[c] += 1
    if len(d) == 2:
        if (d[cards[0]] == 2 or d[cards[0]] == 3):
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
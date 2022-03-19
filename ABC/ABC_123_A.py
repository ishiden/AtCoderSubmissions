import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yay!'
    l = []
    for _ in range(5):
        l.append(int(input()))
    k = int(input())
    if max(l) - min(l) > k:
        ans = ':('
    print(ans)

if __name__ == '__main__':
    main()
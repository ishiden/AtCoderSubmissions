import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    S, T = map(int, input().split())
    ans = T - S + 1
    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    S = list(input().split())
    ans = 'A' + S[1][0] + 'C'
    print(ans)

if __name__ == '__main__':
    main()
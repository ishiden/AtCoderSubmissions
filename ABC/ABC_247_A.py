import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    ans = '0' + S[:-1]
    print(ans)

if __name__ == '__main__':
    main()
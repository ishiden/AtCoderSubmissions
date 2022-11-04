import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'a'
    S = input().rstrip('\n')
    if S == 'a':
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()
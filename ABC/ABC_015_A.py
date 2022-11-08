import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = input().rstrip('\n')
    B = input().rstrip('\n')
    if len(ans) < len(B):
        ans = B
    print(ans)

if __name__ == '__main__':
    main()
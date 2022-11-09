import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'NO'
    M, D = map(int, input().split())
    if M%D == 0:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = '1'
    N = int(input())
    for i in range(1, N):
        ans = ans + ' ' + str(i+1) + ' ' + ans

    print(ans)

if __name__ == '__main__':
    main()
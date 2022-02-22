import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    K = int(input())
    bK = bin(K)
    for k in bK:
        if k == '1':
            ans += '2'
        elif ans != '':
            ans += '0'

    print(ans)

if __name__ == '__main__':
    main()
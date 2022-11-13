import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    mod = 10**4+7
    N = int(input())
    a = [0, 0, 1]
    for i in range(3, N):
        a.append(a[i-3]%mod + a[i-2]%mod + a[i-1]%mod)

    print(a[N-1]%mod)

if __name__ == '__main__':
    main()
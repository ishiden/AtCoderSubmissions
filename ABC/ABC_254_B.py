import bisect
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = [[1]]
    print(1)
    N = int(input())
    for i in range(1, N):
        ans.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                ans[-1].append(1)
            else:
                ans[-1].append(ans[-2][j-1] + ans[-2][j])
        print(' '.join(map(str, ans[-1])))

if __name__ == '__main__':
    main()
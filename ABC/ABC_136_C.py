import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    H = list(map(int, input().split()))
    for i in reversed(range(1, N)):
        if H[i] < H[i-1]:
            if H[i-1] - H[i] > 1:
                ans = 'No'
                break
            else:
                H[i-1] -= 1

    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    A = list(map(int, input().split()))
    all = sum(A)
    if all%10 != 0:
        print(ans)
        exit()
    target = all//10
    A += A
    cur = 0
    start_idx = 0
    for i in range(N*2):
        cur += A[i]
        while cur > target and start_idx <= i:
            cur -= A[start_idx]
            start_idx += 1
        if cur == target:
            ans = 'Yes'
            break

    print(ans)

if __name__ == '__main__':
    main()
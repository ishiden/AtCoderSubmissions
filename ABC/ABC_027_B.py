import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    if 0 < a_sum < N or a_sum%N != 0:
        ans = -1
    else:
        t = 0
        t_p = a_sum//N
        for i in range(N):
            if a[i] == t_p:
                if t == 0:
                    continue
            elif a[i] > t_p:
                t += a[i] - t_p
            else:
                t -= t_p - a[i]
            if t != 0:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
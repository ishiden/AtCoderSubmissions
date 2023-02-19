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
    S = input().rstrip('\n')
    m = [1]
    now = 0
    for i in range(1, N):
        if S[i-1] == S[i]:
            m[now] += 1
        else:
            m.append(1)
            now += 1
    all_range_pattern = N*(N+1)//2
    incident_range_pattern = 0

    for i in range(len(m)):
        incident_range_pattern += m[i]*(m[i]+1)//2

    ans = all_range_pattern - incident_range_pattern

    print(ans)

if __name__ == '__main__':
    main()
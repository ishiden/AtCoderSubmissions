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
    seimei = list()
    for _ in range(N):
        s, t = input().split()
        seimei.append(s)
        seimei.append(t)
    c = collections.Counter(seimei)
    for i in range(0, N*2, 2):
        criteria = 1
        if seimei[i] == seimei[i+1]:
            criteria += 1
        if c[seimei[i]] > criteria and c[seimei[i+1]] > criteria:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    main()
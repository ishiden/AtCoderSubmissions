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
    d = collections.defaultdict(list)
    for i in range(N):
        x, y = map(int, input().split())
        d[y].append([i, x])
    S = input().rstrip('\n')
    for i in d.items():
        mostL, mostR = 1000000001, -1
        for j in i[1]:
            if S[j[0]] == 'L':
                mostR = max(mostR, j[1])
                if j[1] > mostL:
                    ans = 'Yes'
                    break
            elif S[j[0]] == 'R':
                mostL = min(mostL, j[1])
                if j[1] < mostR:
                    ans = 'Yes'
                    break
        if ans == 'Yes':
            break
    print(ans)

if __name__ == '__main__':
    main()
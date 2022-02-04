import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        A, B = map(int, input().split())
        cheese.append([A, B])
    cheese.sort(reverse = True)
    for i in range(N):
        if W <= 0:
            break
        if W >= cheese[i][1]:
            ans += cheese[i][0] * cheese[i][1]
        else:
            ans += cheese[i][0] * W
        W -= cheese[i][1]

    print(ans)

if __name__ == '__main__':
    main()
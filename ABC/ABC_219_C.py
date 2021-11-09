import sys
import collections
import heapq
import itertools
import math
import operator

input = sys.stdin.readline

def main():
    ans = 0
    X = input().rstrip('\n')
    O = 'abcdefghijklmnopqrstuvwxyz'
    dx = {x:o for x, o in zip(X, O)}
    N = int(input())
    S = []
    for i in range(N):
        temp = input().rstrip('\n')
        trans = ''
        for t in temp:
            trans += dx[t]
        S.append([i, trans, temp])
    S.sort(key = operator.itemgetter(1))
    for s in S:
        print(s[2])


if __name__ == '__main__':
    main()
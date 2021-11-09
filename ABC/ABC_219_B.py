import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = ''
    S = []
    for i in range(3):
        S.append(input().rstrip('\n'))
    T = input().rstrip('\n')
    for t in T:
        ans += S[int(t) - 1]
    print(ans)

if __name__ == '__main__':
    main()
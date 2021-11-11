import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    S = list(input().rstrip('\n'))
    N = int(input())
    for _ in range(N):
        l, r = map(int, input().split())
        temps = S[:l-1] + list(reversed(S[l-1:r])) + S[r:]
        S = temps

    print(''.join(S))

if __name__ == '__main__':
    main()
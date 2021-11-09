import sys
import collections
import heapq
import itertools

input = sys.stdin.readline

def main():
    ans = 0
    S, K = input().split()
    S = list(S)
    K = int(K)
    p = itertools.permutations(S, len(S))
    p = list(set(p))
    p.sort()
    print(''.join(p[K-1]))
if __name__ == '__main__':
    main()
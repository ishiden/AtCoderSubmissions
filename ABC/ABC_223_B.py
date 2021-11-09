import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    slist = [S]
    for i in range(len(S)):
        slist.append(S[i:] + S[:i])
    slist.sort()
    print(slist[0])
    print(slist[-1])


if __name__ == '__main__':
    main()
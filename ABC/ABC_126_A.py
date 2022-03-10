import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    N, K = map(int, input().split())
    S = input().rstrip('\n')
    ans = S[:K-1] + S[K-1].lower() + S[K:]
    print(ans)

if __name__ == '__main__':
    main()
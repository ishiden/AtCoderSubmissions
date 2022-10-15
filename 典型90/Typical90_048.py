import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    score_list = []
    for i in range(N):
        A, B = map(int, input().split())
        A -= B
        score_list.append(A)
        score_list.append(B)

    score_list.sort(reverse=True)
    ans = sum(score_list[:K])

    print(ans)

if __name__ == '__main__':
    main()
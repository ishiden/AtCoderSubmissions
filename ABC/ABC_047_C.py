import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
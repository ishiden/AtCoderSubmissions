import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    S, T, X = map(int, input().split())
    if S > T:
        T += 24
        if S > X:
            X += 24
    if S <= X < T:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
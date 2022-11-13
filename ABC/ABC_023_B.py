import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    s = 'b'
    N = int(input())
    S = input().rstrip('\n')
    for i in range(N//2):
        if i%3 == 0:
            s = 'a' + s + 'c'
        elif i%3 == 1:
            s = 'c' + s + 'a'
        else:
            s = 'b' + s + 'b'
        ans = i + 1
    if s != S:
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()
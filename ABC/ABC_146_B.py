import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    S = input().rstrip('\n')
    for s in S:
        x = ord(s) - ord('A')
        x = (x + N) % 26
        print(chr(x + ord('A')), end='')
    print()

if __name__ == '__main__':
    main()
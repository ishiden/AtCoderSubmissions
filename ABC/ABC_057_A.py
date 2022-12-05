import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = (A + B)%24
    print(ans)

if __name__ == '__main__':
    main()
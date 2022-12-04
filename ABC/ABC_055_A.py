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
    ans = N * 800 - N//15*200
    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H1 = int(input())
    H2 = int(input())
    ans = H1 - H2
    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    A, B = input().split()
    ans = int(A + B)*2
    print(ans)

if __name__ == '__main__':
    main()
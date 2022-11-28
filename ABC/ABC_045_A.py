import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    a = int(input())
    b = int(input())
    h = int(input())

    ans = (a + b) * h // 2
    print(ans)

if __name__ == '__main__':
    main()
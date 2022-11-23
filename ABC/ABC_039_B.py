import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    X = int(input())
    ans = 0
    for i in range(1, X+1):
        if i ** 4 == X:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()
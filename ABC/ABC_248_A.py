import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = -1
    S = input()
    for i in range(0, 10):
        if i not in S:
            ans = i

    print(ans)

if __name__ == '__main__':
    main()
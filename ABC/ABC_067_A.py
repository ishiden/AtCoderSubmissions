import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Impossible'
    A, B = map(int, input().split())
    if A%3 == 0 or B%3 ==0 or (A+B)%3 == 0:
        ans = 'Possible'

    print(ans)

if __name__ == '__main__':
    main()
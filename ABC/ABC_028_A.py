import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Bad'
    N = int(input())
    if N == 100:
        ans = 'Perfect'
    elif N >= 90:
        ans = 'Great'
    elif N >= 60:
        ans = 'Good'

    print(ans)

if __name__ == '__main__':
    main()
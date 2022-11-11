import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'ABC'
    if int(input()) == 2:
        ans = 'chokudai'

    print(ans)

if __name__ == '__main__':
    main()
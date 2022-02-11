import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    n = int(input())
    if n > 4 or n == 1 :
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
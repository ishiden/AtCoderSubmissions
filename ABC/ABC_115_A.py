import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    D = int(input())
    ans = 'Christmas' + ' Eve' * (25 - D)

    print(ans)

if __name__ == '__main__':
    main()
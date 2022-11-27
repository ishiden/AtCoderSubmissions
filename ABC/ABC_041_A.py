import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    s = input().rstrip('\n')
    t = int(input())
    print(s[t-1])

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    a = int(input())
    s = input().rstrip('\n')
    if a >= 3200:
        print(s)
    else:
        print('red')

if __name__ == '__main__':
    main()
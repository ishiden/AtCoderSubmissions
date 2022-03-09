import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    S = list(input().rstrip('\n'))
    S.sort()
    print(''.join(S))

if __name__ == '__main__':
    main()
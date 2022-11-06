import collections
import itertools
import math
from operator import indexOf
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    X = input().rstrip('\n')
    s = ['-1', 'A', 'B', 'C', 'D', 'E']
    print(s.index(X))

if __name__ == '__main__':
    main()
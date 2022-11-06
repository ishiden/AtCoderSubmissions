import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    a = int(input())
    b = int(input())
    ans = b - a%b if a%b != 0 else 0
    print(ans)

if __name__ == '__main__':
    main()
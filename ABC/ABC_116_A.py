import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ab, bc, ca = map(int, input().split())
    ans = (ab * bc)//2
    print(ans)

if __name__ == '__main__':
    main()
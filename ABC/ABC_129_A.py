import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    P, Q, R = map(int, input().split())
    ans = P + Q + R - max(P, Q, R)
    print(ans)

if __name__ == '__main__':
    main()
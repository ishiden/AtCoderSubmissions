import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    ans = int(S[0]) * int(S[-1])
    print(ans)

if __name__ == '__main__':
    main()
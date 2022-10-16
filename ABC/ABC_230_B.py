import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    S = input().rstrip('\n')
    if S in "oxxoxxoxxoxx":
        ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()
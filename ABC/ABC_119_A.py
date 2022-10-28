import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Heisei'
    S = input().rstrip('\n')
    if int(S[5:7]) > 4:
        ans = 'TBD'
    print(ans)

if __name__ == '__main__':
    main()
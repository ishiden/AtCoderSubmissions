import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'YES'
    S = input().rstrip('\n')
    S = S.replace('ch', '')
    S = S.replace('o', '')
    S = S.replace('k', '')
    S = S.replace('u', '')
    if S != '':
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
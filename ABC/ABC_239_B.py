import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    X = input().rstrip('\n')
    if X[0] == '-':
        if len(X) == 2:
            ans = '-1'
        else:
            ans = int(X[:-1])
            if X[-1] != '0':
                ans -= 1
    else:
        ans = X[:-1]
    if ans == '':
        ans = '0'
    print(ans)

if __name__ == '__main__':
    main()
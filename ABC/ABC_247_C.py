import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def generateStr(ans, now, N):
    if now != N:
        ans = ans + ' ' + str(now+1) + ' ' + ans
        ans = str.rstrip(ans)
        ans = str.lstrip(ans)
        return generateStr(ans, now + 1, N)
    else:
        return ans

def main():
    ans = ''
    N = int(input())
    ans = generateStr(ans, 0, N)

    print(ans)

if __name__ == '__main__':
    main()
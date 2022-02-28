import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for i in range(1, N+1):
        if len(str(i))%2 == 1:
            ans +=1
    print(ans)

if __name__ == '__main__':
    main()
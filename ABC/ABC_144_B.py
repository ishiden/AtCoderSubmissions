import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    for i in range(1, 10):
        if N%i == 0 and N//i <= 9:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()
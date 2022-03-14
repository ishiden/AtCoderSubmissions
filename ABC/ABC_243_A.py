import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ['F', 'M', 'T']
    V, A, B, C = map(int, input().split())
    family = [A, B, C]
    while V >= 0:
        for i in range(3):
            V -= family[i]
            if V < 0:
                ans = ans[i]
                break
    print(ans)

if __name__ == '__main__':
    main()
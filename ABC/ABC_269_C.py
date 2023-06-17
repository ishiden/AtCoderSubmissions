import bisect
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
    bN = str(bin(N)[2:])
    rBN = bN[::-1]
    l = [['0']]
    if rBN[0] == '1':
        l[-1].append('1')
    for i in range(1, len(bN)):
        l.append([])
        z = ''
        o = ''
        if rBN[i] == '1':
            for j in l[-2]:
                z = '0' + j
                l[-1].append(z)
                o = '1' + j
                l[-1].append(o)
        else:
            for j in l[-2]:
                z = '0' + j
                l[-1].append(z)
    ans = sorted(l[-1])
    for i in ans:
        print(int(i,2))

if __name__ == '__main__':
    main()
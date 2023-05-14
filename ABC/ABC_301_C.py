import collections
import itertools
import math
import re
import sys
import heapq

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def main():
    ans = 'Yes'
    S = input().rstrip('\n')
    T = input().rstrip('\n')
    sc = collections.Counter(S)
    st = collections.Counter(T)

    ct = sc - st
    tc = st - sc

    tmp = 0
    for c, v in ct.items():
        if c != '@' and c not in 'atcoder':
            ans = 'No'
            break
        if c != '@':
            tmp += v

    tmp2 = 0
    for c, v in tc.items():
        if c != '@' and c not in 'atcoder':
            ans = 'No'
            break
        if c != '@':
            tmp2 += v
    if tmp > st['@'] or tmp2 > sc['@']:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()
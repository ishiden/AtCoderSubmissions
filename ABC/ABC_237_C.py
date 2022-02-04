import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    S = input().rstrip('\n')
    sc, ec = 0, 0
    l = len(S)
    if S[0] == 'a':
        while sc < l and S[sc] == 'a':
            sc += 1
    if S[-1] == 'a':
        while ec < l and S[-(ec+1)] == 'a':
            ec += 1
    if sc > ec:
        ans = 'No'
    else:
        s = S[max(0, sc-1):l - ec]
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                ans = 'No'
                break
    print(ans)

if __name__ == '__main__':
    main()
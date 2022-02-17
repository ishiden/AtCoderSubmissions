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
    for i in range(len(S)):
        if i%2 != 0:
            if S[i] == 'R':
                ans = 'No'
                break
        else:
            if S[i] == 'L':
                ans = 'No'
                break

    print(ans)

if __name__ == '__main__':
    main()
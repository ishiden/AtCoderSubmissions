import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    N = int(input())
    S = input().rstrip('\n')
    ansl = [str(N)]
    ansr = []
    for i in reversed(range(N)):
        if S[i] == 'L':
            ansl.append(str(i))
        else:
            ansr.append(str(i))
    ans = ansr[::-1] + ansl
    print(' '.join(ans))

if __name__ == '__main__':
    main()
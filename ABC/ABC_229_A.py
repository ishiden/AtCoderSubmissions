import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'No'
    S1 = input().rstrip('\n')
    S2 = input().rstrip('\n')
    if S1 == '##' or S2 == '##':
        ans = 'Yes'
    elif S1[0] == S2[0] == '#' or S1[1] == S2[1] == '#':
        ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()
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
    T = input().rstrip('\n')
    K = (ord(T[0]) - ord(S[0]))%26
    for i in range(1, len(S)):
        if (ord(T[i]) - ord(S[i]))%26 != K:
            ans = 'No'
            break

    print(ans)

if __name__ == '__main__':
    main()
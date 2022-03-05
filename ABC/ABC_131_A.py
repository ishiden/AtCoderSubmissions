import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'Good'
    S = input().rstrip('\n')
    for i in range(3):
        if S[i] == S[i+1]:
            ans = 'Bad'
    print(ans)

if __name__ == '__main__':
    main()
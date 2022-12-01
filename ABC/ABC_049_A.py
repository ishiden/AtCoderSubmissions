import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'consonant'
    c = input().rstrip('\n')
    if c in ['a', 'e', 'i', 'o', 'u']:
        ans = 'vowel'
    print(ans)

if __name__ == '__main__':
    main()
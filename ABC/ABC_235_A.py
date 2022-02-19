import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    s = input().rstrip('\n')
    for i in range(3):
        ans += int(s[i])
        ans += int(s[i])*10
        ans += int(s[i])*100

    print(ans)

if __name__ == '__main__':
    main()
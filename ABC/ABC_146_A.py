import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    l = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    for i in range(7):
        if S == l[i]:
            ans = 7 - i
            break
    print(ans)

if __name__ == '__main__':
    main()
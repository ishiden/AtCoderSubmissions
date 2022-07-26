import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    N = int(input())
    user_dict = dict()
    for i in range(N):
        s = input()
        if s not in user_dict:
            user_dict[s] = i
            ans += str(i+1) + "\n"
    print(ans)

if __name__ == '__main__':
    main()
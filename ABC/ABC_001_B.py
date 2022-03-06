import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def func(M):
    if M < 100:
        return 0
    elif M <= 5000:
        return M//100
    elif M <= 30000:
        return M//1000 + 50
    elif M <= 70000:
        return (M//1000 - 30)//5 + 80
    else:
        return 89

def main():
    ans = 0
    m = int(input())
    ans = str(func(m))
    if len(ans) == 1:
        ans = '0' + ans
    print(ans)

if __name__ == '__main__':
    main()
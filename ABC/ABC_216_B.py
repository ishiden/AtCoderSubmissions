import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    names = []
    for _ in range(N):
        name = input()
        if name not in names:
            names.append(name)
        else:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()
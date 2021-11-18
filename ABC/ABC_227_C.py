import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for i in range(1, N+1):
        if i * i * i > N:
            break
        for j in range(i, N+1):
            if i * j * j > N:
                break
            ans += N // i // j - j + 1
    print(ans)

if __name__ == '__main__':
    main()
import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 1
    N = int(input())
    A = list(map(int, input().split()))
    a = sorted(A)
    print(A.index(a[-2]) + 1)

if __name__ == '__main__':
    main()
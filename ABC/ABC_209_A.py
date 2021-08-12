import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = B - A + 1
    print(max(ans, 0))

if __name__ == '__main__':
    main()
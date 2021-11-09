import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    ans = A^B
    print(ans)

if __name__ == '__main__':
    main()
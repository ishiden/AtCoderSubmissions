import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    if N >= 212:
        ans = 8
    elif N >= 126:
        ans = 6
    else:
        ans = 4
    print(ans)

if __name__ == '__main__':
    main()
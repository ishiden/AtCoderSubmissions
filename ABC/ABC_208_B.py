import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    P = int(input())
    cl = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    cl.sort(reverse=True)
    while P != 0:
        for c in cl:
            if P >= c:
                ans += P // c
                P -= P // c * c

    print(ans)

if __name__ == '__main__':
    main()
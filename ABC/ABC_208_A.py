import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 'Yes'
    A, B = map(int, input().split())
    if B / A > 6 or B < A:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()
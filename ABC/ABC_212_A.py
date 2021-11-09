import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = ''
    A, B = map(int, input().split())
    if B == 0:
        ans = 'Gold'
    elif A == 0:
        ans = 'Silver'
    else:
        ans = 'Alloy'

    print(ans)

if __name__ == '__main__':
    main()
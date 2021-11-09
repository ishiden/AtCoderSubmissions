import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 'WA'
    S = input().rstrip('\n')
    if S == 'Hello,World!':
        ans = 'AC'

    print(ans)

if __name__ == '__main__':
    main()
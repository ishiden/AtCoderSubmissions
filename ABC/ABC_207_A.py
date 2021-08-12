import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    Cards = list(map(int, input().split()))
    Cards.sort()
    ans = Cards[1] + Cards[2]

    print(ans)

if __name__ == '__main__':
    main()
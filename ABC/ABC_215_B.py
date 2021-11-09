import sys
import collections
import heapq
import math

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    tmp = 1
    for i in range(N):
        if N >= tmp*2:
            tmp *= 2
            ans +=1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
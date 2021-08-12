import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C, D = map(int, input().split())
    if A + B == C * D:
        ans = 1
    elif B >= C * D:
        ans = -1
    else:
        for i in range(10**5 + 1):
            if A + B*i <= C*D*i:
                ans = i
                break
    print(ans)

if __name__ == '__main__':
    main()
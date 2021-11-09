import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S, T = map(int, input().split())
    for i in range(S+1):
        if i > S:
            break
        for j in range(S+1):
            if i + j > S:
                break
            for k in range(S+1):
                if i + j + k > S:
                    break
                if i * j * k > T:
                    break
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
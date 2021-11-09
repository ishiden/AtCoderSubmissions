import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N, K = map(int, input().split())
    C = list(input().split())
    d = collections.defaultdict(int)
    for i in range(K):
        d[C[i]] += 1
    ans = len(d)

    for i in range(K, N):
        d[C[i]] += 1
        d[C[i-K]] -= 1
        if d[C[i-K]] == 0:
            del d[C[i-K]]
        ans = max(ans, len(d))


    print(ans)

if __name__ == '__main__':
    main()
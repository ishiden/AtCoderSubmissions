import sys

input = sys.stdin.readline

def main():
    ans = 'IMPOSSIBLE'
    l1 = set()
    lN = set()
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        if a == 1:
            l1.add(b)
        elif b == N:
            lN.add(a)
    if l1 & lN:
        ans = 'POSSIBLE'

    print(ans)

if __name__ == '__main__':
    main()
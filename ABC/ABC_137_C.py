import sys
from collections import Counter

input = sys.stdin.readline

def main():
    ans = 0
    l = []
    N = int(input())
    for _ in range(N):
        l.append(''.join(sorted(list(input().rstrip('\n')))))
    l.sort()
    c = 1
    for i in range(N):
        if i < N - 1 and l[i] == l[i + 1]:
            c += 1
        else:
            if c > 2:
                ans += c * (c - 1) // 2
            elif c == 2:
                ans += 1
            c = 1

    print(ans)

if __name__ == '__main__':
    main()
import sys
from collections import Counter

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    for val, cnt in c.items():
        if val > cnt:
            ans += cnt
        elif cnt > val:
            ans += cnt - val

    print(ans)

if __name__ == '__main__':
    main()
import sys

from collections import Counter

input = sys.stdin.readline

def main():
    ans = 'NO'
    S = input().rstrip('\n')
    c = Counter(S)
    if 0 <= c['a'] - c['b'] <= 1 and 0 <= c['a'] - c['c'] <= 1 and 0 <= c['c'] - c['b'] <= 1:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()
import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 'Strong'
    s = '01234567890123456789'
    X = input().rstrip('\n')
    if len(set(list(X))) == 1:
        ans = 'Weak'
    if X in s:
        ans = 'Weak'

    print(ans)

if __name__ == '__main__':
    main()
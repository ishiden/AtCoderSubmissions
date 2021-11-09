import sys
import collections
import heapq

input = sys.stdin.readline

def check(target):
    c = 0
    for t in target:
        if t == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            return False
    return c == 0

def main():
    ans = 0
    N = int(input())
    l = []

    if N%2 != 0:
        ans = ''
    else:
        for i in range(2**N):
            S = ''
            for j in range(N):
                if (i >> j) & 1:
                    S += ')'
                else:
                    S += '('
            if check(S):
                l.append(S)
    l.sort()
    for s in l:
      print(s)

if __name__ == '__main__':
    main()
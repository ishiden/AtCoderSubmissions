import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'Yes'
    S = list(input().rstrip('\n'))
    T = list(input().rstrip('\n'))
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i] == T[i + 1]:
                T[i], T[i+1] = T[i+1], T[i]
            else:
                ans = 'No'
                break
    if S != T:
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()
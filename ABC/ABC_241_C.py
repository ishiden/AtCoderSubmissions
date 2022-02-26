import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    S = []
    S3 = []
    for _ in range(N):
        temp = input().rstrip('\n')
        S.append(temp)
        S3.append(temp[::-1])
    S2 = [''.join(x) for x in zip(*S)]

    T = ['######',
         '#####.', '####.#', '###.##', '##.###', '#.####', '.#####',
         '..####', '.#.###', '.##.##', '.###.#', '.####.',
         '#..###', '#.#.##', '#.##.#', '#.###.',
         '##..##', '##.#.#', '##.##.',
         '###..#', '###.#.',
         '####..']

    for i in range(N):
        if ans == 'Yes':
            break
        for t in T:
            if t in S[i] or t in S2[i]:
                ans = 'Yes'
                break

    for i in range(N):
        if ans == 'Yes':
            break
        temp = ''
        temp2 = ''
        temp3 = ''
        temp4 = ''
        for j in range(N):
            if i + j >= N:
                break
            temp += S[j][i+j]
            temp2 += S[i+j][j]
            temp3 += S3[j][i+j]
            temp4 += S3[i+j][j]

        for t in T:
            if t in temp or t in temp2 or t in temp3 or t in temp4:
                ans = 'Yes'
                break

    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    Q = int(input())
    que = collections.deque()
    for _ in range(Q):
        q = input().split()
        if q[0] == '1':
            que.append((int(q[1]), int(q[2])))
        else:
            tmp = 0
            iq = int(q[1])
            while iq > 0:
                b = que.popleft()
                tmp += b[0]*min(iq, b[1])
                if b[1] > iq:
                    que.appendleft((b[0], b[1]-iq))
                iq -= b[1]
            print(tmp)

if __name__ == '__main__':
    main()
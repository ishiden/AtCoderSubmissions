import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

class UnionFind():
    par = []
    siz = []

    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y: return False

        if self.siz[x] < self.siz[y]: x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]

        return True

    def size(self, x):
        return self.siz[self.root(x)]

def main():
    ans = 0
    N, M = map(int, input().split())
    g = UnionFind(N)
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g.unite(u, v)

    for i in range(N):
        if g.root(i) == i:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
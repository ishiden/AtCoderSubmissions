import sys
import collections
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
    N = int(input())
    A = list(map(int, input().split()))
    uf = UnionFind(2*10**5 + 1)
    for i in range(N//2):
        if A[i] != A[-1 * (i + 1)]:
            if not uf.is_same(A[i], A[-1 * (i + 1)]):
                ans += 1
                uf.unite(A[i], A[-1 * (i + 1)])
    print(ans)

if __name__ == '__main__':
    main()
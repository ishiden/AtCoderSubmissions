import sys

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
    l = []

    N, M = map(int, input().split())

    for i in range(M):
        a, b = map(int, input().split())
        l.append([a, b])

    for i in range(M):
        u = UnionFind(N)
        for j in range(M):
            if i != j:
                u.unite(l[j][0] - 1, l[j][1] - 1)
        for k in range(N):
            if not u.is_same(0, k):
                ans += 1
                break

    print(ans)

if __name__ == '__main__':
    main()
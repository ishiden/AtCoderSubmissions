import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

inf = float('INF')

def dijkstra(n, g, s):
    dist = [inf for _ in range(n)]
    dist[s] = 0
    hq = []
    heapq.heappush(hq, (dist[s], s))

    while len(hq) != 0:
        e = heapq.heappop(hq)
        v = e[1]
        d = e[0]

        if d > dist[v]:
            continue

        for to, w in g[v]:
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                heapq.heappush(hq, (dist[to], to))

    return dist


def main():
    ans = 0

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        G[a].append([b, c])
        G[b].append([a, c])

    d_from0 = dijkstra(N, G, 0)
    d_fromN = dijkstra(N, G, N-1)

    for i in range(N):
        ans = d_from0[i] + d_fromN[i]
        print(ans)

if __name__ == '__main__':
    main()
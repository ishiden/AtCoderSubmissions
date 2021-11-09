import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    H, W, N = map(int, input().split())
    X, Y = [], []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    Xdict = {x:i+1 for i, x in enumerate(sorted(list(set(X))))}
    Ydict = {y:i+1 for i, y in enumerate(sorted(list(set(Y))))}

    for i in range(N):
        print(Xdict[X[i]], Ydict[Y[i]])

if __name__ == '__main__':
    main()
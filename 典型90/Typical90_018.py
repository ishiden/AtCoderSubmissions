import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def calcCoordinate(t, e, l):
    rx = 0
    ry = -l/2*math.sin(math.radians(360*e/t))
    rz = l/2 - l/2*math.cos(math.radians(360*e/t))
    return (rx, ry, rz)

def calcAngle(x, y, ry, rz):
    a = (x**2 + (ry - y)**2)**0.5
    return math.atan2(rz, a)

def main():
    ans = 0
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    for _ in range(Q):
        E = int(input())
        coo = calcCoordinate(T, E, L)
        ans = calcAngle(X, Y, coo[1], coo[2])
        print(math.degrees(ans))

if __name__ == '__main__':
    main()
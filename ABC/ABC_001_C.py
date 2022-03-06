import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def my_round(val, degit=0):
    p = 10 ** degit
    return (val * p * 2 + 1) // 2 / p

def main():
    deg = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    dis = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
    Deg, Dis = map(int, input().split())
    g = deg[int(((Deg * 10 + 1125) / 2250) % 16)]
    s = -1
    for i in range(len(dis)):
        if my_round(Dis/60, 1) <= dis[i]:
            s = i
            break
    if s == -1:
        s = 12
    elif s == 0:
        g = 'C'

    print(g, s)

if __name__ == '__main__':
    main()
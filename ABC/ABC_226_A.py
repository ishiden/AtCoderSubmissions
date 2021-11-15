import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    X = float(input())
    print(int(round(X+0.0005, 0)))

if __name__ == '__main__':
    main()
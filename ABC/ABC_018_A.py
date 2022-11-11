import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    l = list()
    for i in range(3):
        l.append([i, int(input())])
    ll = sorted(l, key=lambda x:x[1], reverse=True)
    for i in range(3):
        print(ll.index(l[i])+1)
if __name__ == '__main__':
    main()
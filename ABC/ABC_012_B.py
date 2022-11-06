import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    S = int(input())
    h = S//3600
    m = (S - h*3600)//60
    s = S - h*3600 - m*60
    print(str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2))

if __name__ == '__main__':
    main()
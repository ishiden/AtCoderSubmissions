import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    l = [
    213456, 231456, 234156, 234516, 234561,
    324561, 342561, 345261, 345621, 345612,
    435612, 453612, 456312, 456132, 456123,
    546123, 564123, 561423, 561243, 561234,
    651234, 615234, 612534, 612354, 612345,
    162345, 126345, 123645, 123465, 123456
    ]

    print(l[N%30-1])

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    s1, s2, s3 = input().split()
    ans = s1[0] + s2[0] + s3[0]
    print(str.upper(ans))

if __name__ == '__main__':
    main()
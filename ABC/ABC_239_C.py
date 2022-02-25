import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    x1, y1, x2, y2 = map(int, input().split())
    pl1 = [[x1+1, y1+2], [x1+1, y1-2], [x1+2, y1+1], [x1+2, y1-1]
          ,[x1-1, y1+2], [x1-1, y1-2], [x1-2, y1+1], [x1-2, y1-1]]
    pl2 = [[x2+1, y2+2], [x2+1, y2-2], [x2+2, y2+1], [x2+2, y2-1]
          ,[x2-1, y2+2], [x2-1, y2-2], [x2-2, y2+1], [x2-2, y2-1]]
    for i in range(8):
        for j in range(8):
            if pl1[i] == pl2[j]:
                ans = 'Yes'
                break
    print(ans)

if __name__ == '__main__':
    main()
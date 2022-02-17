import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    W = ['Sunny', 'Cloudy', 'Rainy'] * 2
    S = input().rstrip('\n')
    for i in range(3):
        if W[i] == S:
            print(W[i+1])
            break

if __name__ == '__main__':
    main()
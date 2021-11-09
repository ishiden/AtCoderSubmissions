import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    s = list()
    for _ in range(4):
        s.append(input())
    ss = set(s)
    if len(ss) == 4:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
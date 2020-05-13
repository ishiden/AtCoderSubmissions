import sys
import itertools

input = sys.stdin.readline

def main():
    a = b = 0
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    d = [1,2,3,4,5,6,7,8,9]

    prm = list(itertools.permutations(d[:n], n))

    a = prm.index(p) + 1
    b = prm.index(q) + 1

    print(abs(a-b))

if __name__ == '__main__':
    main()
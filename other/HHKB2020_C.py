import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    p = list(map(int, input().split()))
    cl = [0]*200002
    at = 0
    for i in range(N):
        cl[p[i]] += 1
        while cl[at]:
            at += 1
        print(at)

if __name__ == '__main__':
    main()
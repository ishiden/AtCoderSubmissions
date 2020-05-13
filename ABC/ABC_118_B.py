import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    f = set(range(1,M+1))
    for _ in range(N):
        a = set(list(map(int, input().split()))[1:])
        f.intersection_update(a)
    print(len(f))

if __name__ == '__main__':
    main()
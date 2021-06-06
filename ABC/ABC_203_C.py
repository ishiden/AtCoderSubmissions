import sys

input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    l = []
    for i in range(N):
        A, B = map(int, input().split())
        l.append([A, B])
    l.sort()
    for i in range(N):
        if l[i][0] > K:
            break
        K += l[i][1]

    print(K)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            temp = (A[j][0]-A[i][0])**2 + (A[j][1]-A[i][1])**2
            ans = max(ans, temp)
    print('{:.20}'.format(ans**0.5))

if __name__ == '__main__':
    main()
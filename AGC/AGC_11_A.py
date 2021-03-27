import sys

input = sys.stdin.readline

def main():
    ans = 1
    N, C, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(int(input()))
    T.sort()
    tmp_c = 1
    tmp_dtime = T[0] + K
    for i in range(1, N):
        if tmp_c < C and T[i] <= tmp_dtime:
            tmp_c += 1
        else:
            ans += 1
            tmp_c = 1
            tmp_dtime = T[i] + K
    print(ans)

if __name__ == '__main__':
    main()
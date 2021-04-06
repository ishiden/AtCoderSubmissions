import sys

input = sys.stdin.readline

def main():
    ans = 0
    all_a = 0
    l = []
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        all_a += A
        l.append([2 * A + B, A, B])
    l.sort(key = lambda x: x[0], reverse = True)
    for i in range(N):
        all_a -= l[i][0]
        ans += 1
        if all_a < 0:
            break

    print(ans)

if __name__ == '__main__':
    main()
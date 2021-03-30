import sys

input = sys.stdin.readline

def main():
    ans = 0
    W, H, N = map(int, input().split())
    lb = [0, 0]
    rt = [W, H]
    for i in range(N):
        x, y, a = map(int, input().split())
        if a == 1:
            lb[0] = max(lb[0], x)
        elif a == 2:
            rt[0] = min(rt[0], x)
        elif a == 3:
            lb[1] = max(lb[1], y)
        else:
            rt[1] = min(rt[1], y)

    if lb[0] < rt[0] and lb[1] < rt[1]:
        ans = (rt[0] - lb[0]) * (rt[1] - lb[1])

    print(ans)

if __name__ == '__main__':
    main()
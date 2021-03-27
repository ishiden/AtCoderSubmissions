import sys

input = sys.stdin.readline

def main():
    ans = 0
    W, H, x, y = map(int, input().split())
    ans = W * H / 2
    ans2 = 0
    if x*2 == W and y*2 == H:
        ans2 = 1
    print('{:.10f}'.format(ans), ans2)

if __name__ == '__main__':
    main()
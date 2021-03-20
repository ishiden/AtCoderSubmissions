import sys

input = sys.stdin.readline

def main():
    ans_min, ans_max = 10**9, -1
    A, B, W = map(int, input().split())
    W *= 1000
    for i in range(10**6):
        if W >= i * A and W <= i * B:
            ans_min = min(ans_min, i)
            ans_max = max(ans_max, i)

    print('UNSATISFIABLE' if ans_max == -1 else (str(ans_min) + " " + str(ans_max)))

if __name__ == '__main__':
    main()
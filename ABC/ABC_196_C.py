import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    for i in range(1, 1000001):
        if int(str(i) + str(i)) <= N:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
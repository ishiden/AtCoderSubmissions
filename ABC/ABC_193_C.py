import sys

input = sys.stdin.readline

def main():
    N = int(input())
    s = set()
    for a in range(2, int(N ** 0.5) + 1):
        tmp = a * a
        while tmp <= N:
            s.add(tmp)
            tmp *= a

    print(N - len(s))

if __name__ == '__main__':
    main()
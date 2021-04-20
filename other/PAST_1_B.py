import sys

input = sys.stdin.readline

def main():
    N = int(input())
    prev = int(input())
    for i in range(N-1):
        A = int(input())
        if A == prev:
            print('stay')
        elif A > prev:
            print('up', A - prev)
        else:
            print('down', prev - A)
        prev = A

if __name__ == '__main__':
    main()
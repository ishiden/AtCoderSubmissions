import sys

input = sys.stdin.readline

def main():
    ans = 0
    A, B = map(int, input().split())
    Y = (A-B)//2
    X = B + Y
    print(X, Y)

if __name__ == '__main__':
    main()
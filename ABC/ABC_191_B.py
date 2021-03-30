import sys

input = sys.stdin.readline

def main():
    ans = 0
    N, X = input().split()
    A = list(input().split())
    ans = [i for i in A if i != X]
    print(' '.join(ans))

if __name__ == '__main__':
    main()
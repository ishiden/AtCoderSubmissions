import sys

input = sys.stdin.readline

def main():
    d = '"'
    S = input().rstrip('\n')
    A, B, C, D = map(int, input().split())
    print(S[:A]+d+S[A:B]+d+S[B:C]+d+S[C:D]+d+S[D:])

if __name__ == '__main__':
    main()

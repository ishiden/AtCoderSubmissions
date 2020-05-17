import sys

input = sys.stdin.readline

def main():
    K = int(input())
    S = input().rstrip('\n')
    if len(S) > K:
        print(S[:K]+'...')
    else:
        print(S)

if __name__ == '__main__':
    main()
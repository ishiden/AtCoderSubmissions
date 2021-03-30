import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    V, T, S, D = map(int, input().split())
    if V * T <= D <= V * S:
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()
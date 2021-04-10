import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H > sum(A):
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()
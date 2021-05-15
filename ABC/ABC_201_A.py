import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    A = list(map(int, input().split()))
    A.sort()
    if A[2] - A[1] == A[1] - A[0]:
        ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k,n):
        if a[i-k]<a[i]:
            print('Yes')
        else:
            print("No")

if __name__ == '__main__':
    main()
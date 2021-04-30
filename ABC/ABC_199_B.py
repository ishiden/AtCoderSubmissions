import sys

input = sys.stdin.readline

def main():
    ans = 0
    N =  int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans  = min(B)  -  max(A) + 1

    print(ans if ans >= 0 else  0)

if __name__ == '__main__':
    main()
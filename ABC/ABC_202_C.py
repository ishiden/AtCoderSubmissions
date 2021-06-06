import sys
import collections

input = sys.stdin.readline

def CCounter(s):
    return collections.Counter(s)

def main():
    ans = 0
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    a_c = CCounter(A)
    c_c = CCounter(C)

    for i in range(N):
        a = a_c[B[i]]
        if a  > 0:
            ans += a * c_c[i+1]
    print(ans)

if __name__ == '__main__':
    main()
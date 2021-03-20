import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    a2, b2 = 10**5 + 1, 10**5 + 1
    aa, bb = 0, 0
    a, b = map(int, input().split())

    for i in range(N-1):
        A, B = map(int, input().split())

        if A < a:
            a2 = a
            a = A
            aa = i + 1
        elif A < a2:
            a2 = A
        if B < b:
            b2 = b
            b = B
            bb = i + 1
        elif B < b2:
            b2 = B
    if aa != bb :
        ans = max(a,b)
    else:
        ans = min(a+b, min(max(a, b2), max(a2, b)))

    print(ans)

if __name__ == '__main__':
    main()
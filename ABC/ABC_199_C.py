import sys

input = sys.stdin.readline

def main():
    ans = ''
    N = int(input())
    S = list(input().rstrip('\n'))
    S1 = S[:N]
    S2 = S[N:]
    Q = int(input())
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            if A > N:
                A -= N
                B -= N
                tmp = S2[A-1]
                S2[A-1] = S2[B-1]
                S2[B-1] = tmp
            elif B > N:
                B -= N
                tmp = S1[A-1]
                S1[A-1] = S2[B-1]
                S2[B-1] = tmp
            else:
                tmp = S1[A-1]
                S1[A-1] = S1[B-1]
                S1[B-1] = tmp

        elif T == 2:
            tmp = S1
            S1 = S2
            S2 = tmp
    ans = ''.join(S1 + S2)
    print(ans)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    ans = 0
    A  = input().rstrip('\n')
    B  = input().rstrip('\n')
    C  = input().rstrip('\n')
    la, lb, lc = len(A) + 1, len(B), len(C)
    ia, ib, ic = 0, 0, 0
    next = 'a'
    while True:
        if next == 'a':
            if ia == la - 1:
                ans = next
                break
            else:
                next = A[ia]
                ia += 1
        elif next == 'b':
            if ia == lb - 1:
                ans = next
                break
            else:
                next = B[ib]
                ib += 1
        elif next == 'c':
            if ia == lc - 1:
                ans = next
                break
            else:
                next = C[ic]
                ic += 1
    print(next.upper())

if __name__ == '__main__':
    main()
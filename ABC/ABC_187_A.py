import sys

input = sys.stdin.readline

def main():
    A, B = input().split()
    int_A = int(A[0]) + int(A[1]) + int(A[2])
    int_B = int(B[0]) + int(B[1]) + int(B[2])
    print(int_A if int_A > int_B else int_B)

if __name__ == '__main__':
    main()
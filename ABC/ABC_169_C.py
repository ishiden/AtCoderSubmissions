import sys
import math

input = sys.stdin.readline

def main():
    ans = 0
    A, B = input().split()
    B = B.replace(".", "")
    ans = int(A) * int(B)
    ans = str(ans)[:-2]
    if ans == "":
        ans = "0"
    print(ans)

if __name__ == '__main__':
    main()
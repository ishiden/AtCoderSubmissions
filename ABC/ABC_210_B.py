import sys
import collections
import heapq

input = sys.stdin.readline

def main():
    ans = ""
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                ans = "Takahashi"
            else:
                ans = "Aoki"
            break

    print(ans)

if __name__ == '__main__':
    main()
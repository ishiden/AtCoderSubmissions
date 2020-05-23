import sys

input = sys.stdin.readline

def main():
    ans = []
    N = int(input())
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i+N//i-2)
    print(min(ans))

if __name__ == '__main__':
    main()

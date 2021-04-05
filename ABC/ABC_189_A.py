import sys

input = sys.stdin.readline

def main():
    ans = 'Lost'
    C = input()
    if C[0] == C[1] and C[1] == C[2]:
        ans = 'Won'
    print(ans)

if __name__ == '__main__':
    main()
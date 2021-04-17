import sys

input = sys.stdin.readline

def judge(n):
    if n % 4 == 0:
        return 'Even'
    elif n % 2 == 0:
        return 'Same'
    else:
        return 'Odd'

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print(judge(N))

if __name__ == '__main__':
    main()
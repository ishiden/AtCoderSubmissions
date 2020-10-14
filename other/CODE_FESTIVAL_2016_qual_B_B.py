import sys

input = sys.stdin.readline

def main():
    a = 'a'
    b = 'b'
    y = 'Yes'
    n = 'No'
    ac = 0
    bc = 0
    N, A, B = map(int, input().split())
    s = input()
    for i in range(N):
        if s[i] == a:
            if ac < A + B:
                print(y)
                ac += 1
            else:
                print(n)
        elif s[i] == b:
            if ac < A + B and bc+1 <= B:
                print(y)
                ac += 1
                bc += 1
            else:
                print(n)
        else:
            print(n)

if __name__ == '__main__':
    main()
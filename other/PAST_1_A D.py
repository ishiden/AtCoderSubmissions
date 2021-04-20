import sys

input = sys.stdin.readline

def main():
    ans = 'Correct'
    n = 0
    w = 0
    N = int(input())
    l = [0] * N
    for i in range(N):
        A = int(input())
        l[A - 1] += 1
    for i in range(N):
        if l[i] == 0:
            n = i + 1
        if l[i] == 2:
            w = i + 1
    if n != 0:
        print(w, n)
    else:
        print(ans)

if __name__ == '__main__':
    main()
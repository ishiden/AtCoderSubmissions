import sys

input = sys.stdin.readline

def main():
    l = [2, 1]
    N = int(input())
    for i in range(N-1):
        l.append(l[i]+l[i+1])
    print(l[N])

if __name__ == '__main__':
    main()
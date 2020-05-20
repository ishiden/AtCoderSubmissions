import sys

input = sys.stdin.readline

def main():
    N = int(input())
    sl = [input().split() + [i+1] for i in range(N)]
    sl.sort(key=lambda x: (x[0], -int(x[1])))
    for i in sl:
        print(i[2])

if __name__ == '__main__':
    main()
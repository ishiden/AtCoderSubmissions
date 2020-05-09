import sys

input = sys.stdin.readline

def main():
    n = int(input())
    o = list(map(int, input().split()))
    l = [0]*n
    for i in range(n):
        l[o[i]-1] = i+1
    print(" ".join(map(str,l)))

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    l = []
    N = int(input())
    T, A = map(int, input().split())
    h = list(map(int, input().split()))
    for  i in range(N):
      l.append(abs(A-(T-h[i]*0.006)))
    print(l.index(min(l))+1)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    if N%1000 == 0:
      ans = 1000*((N//1000))-N
    else:
      ans = 1000*((N//1000)+1)-N
    print(ans)

if __name__ == '__main__':
    main()
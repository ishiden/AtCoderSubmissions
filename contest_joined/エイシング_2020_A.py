import sys

input = sys.stdin.readline

def main():
    l,r,d = map(int, input().split())
    print(r//d - (l-1)//d)

if __name__ == '__main__':
    main()
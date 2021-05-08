import sys

input = sys.stdin.readline

def main():
    ans = 0
    t = 'ZONe'
    S = input().rstrip('\n')
    ans = S.count(t)
    print(ans)

if __name__ == '__main__':
    main()
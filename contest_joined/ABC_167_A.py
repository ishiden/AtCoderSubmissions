import sys

input = sys.stdin.readline

def main():
    s = list(input().rstrip('\n'))
    t = list(input())
    if t[:len(s)] == s:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
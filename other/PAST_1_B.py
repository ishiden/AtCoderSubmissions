import sys

input = sys.stdin.readline

def main():
    words = ['stay', 'down', 'up']
    n = int(input())
    t = int(input())
    for i in range(n-1):
        c = int(input())
        d = t - c
        if d == 0:
            print(words[0])
        elif d > 0:
            print(words[1], abs(d))
        else:
            print(words[2], abs(d))
        t = c

if __name__ == '__main__':
    main()
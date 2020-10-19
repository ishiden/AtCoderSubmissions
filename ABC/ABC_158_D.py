import sys

input = sys.stdin.readline

def main():
    s = input().rstrip('\n')
    Q = int(input())
    r = False
    for _ in range(Q):
        t = input().rstrip('\n')
        if t == '1':
            r = not r
        else:
            t, f, c = t.split()
            if (f == '1' and not r) or (f == '2' and r):
                s = c + s
            else:
                s += c
    print(s if r else s[::-1])

if __name__ == '__main__':
    main()
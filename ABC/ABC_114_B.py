import sys

input = sys.stdin.readline

def main():
    ans = 753
    s = input()
    for i in range(len(s)-2):
        t = int(s[i:i+3])
        ans = min(ans, abs(753-t))
    print(ans)

if __name__ == '__main__':
    main()
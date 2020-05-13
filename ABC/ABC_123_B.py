import sys

input = sys.stdin.readline

def main():
    ans = 0
    ex = []
    for _ in range(5):
        t = int(input())
        e = 10 - t%10
        if e != 10:
          ex.append(e)
        ans += t
    ex.sort()
    ans += sum(ex[:-1])

    print(ans)

if __name__ == '__main__':
    main()
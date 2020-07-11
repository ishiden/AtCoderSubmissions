import sys

input = sys.stdin.readline

def main():
    ans = [0]* 10010
    n = int(input())
    v = (x+y+z)**2 - x*y - y*z - z*x
    for x in range(1,101):
        for y in range(1,101):
            for z in range(1,101):
                if v <= n:
                    ans[n] += 1
    for i in range(1,n+1):
        print(ans[i])

if __name__ == '__main__':
    main()
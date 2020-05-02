def main():
    ans = 0
    a,b,n = map(int, input().split())
    n = min(b-1, n)
    ans = (a*n)//b - a*(n//b)
    print(ans)

if __name__ == '__main__':
    main()
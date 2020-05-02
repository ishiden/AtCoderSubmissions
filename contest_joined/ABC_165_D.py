def main():
    ans = 0
    a,b,n = map(int, input().split())
    if b > n:
        ans = (a*n)//b - a*(n//b)
    else:
        ans = (a*(b-1))//b - a*((b-1)//b)
    print(ans)

if __name__ == '__main__':
    main()
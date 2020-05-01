def main():
    ans = 0
    mod = 10**9+7
    a,b,c = map(int, input().split())
    ans = a*b*c%mod
    print(ans)

if __name__ == '__main__':
    main()
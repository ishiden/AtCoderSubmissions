def main():
    ans = 0
    n,m = map(int, input().split())
    p = m//2
    if p >= n:
        ans += n + (p-n)//2
    else:
        ans += p
    print(ans)

if __name__ == '__main__':
    main()
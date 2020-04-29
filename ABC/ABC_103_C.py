def main():
    ans = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in l:
        ans += i - 1
    print(ans)

if __name__ == '__main__':
    main()
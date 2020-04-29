def main():
    ans = 0
    n = int(input())
    l = list(map(int, input().split()))
    ans = sum(l)-n
    print(ans)

if __name__ == '__main__':
    main()
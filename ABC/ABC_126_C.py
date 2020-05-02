def main():
    ans = 0
    n, k = map(int, input().split())
    for i in range(1,n+1):
        temp = 1/n
        eye = i
        while(eye < k):
            eye *= 2
            temp /= 2
        ans += temp
    print(ans)

if __name__ == '__main__':
    main()
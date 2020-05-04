def main():
    ans = 0
    n,k = map(int, input().split())
    l = [0]*n
    for i in range(k):
        d = int(input())
        s = list(map(int, input().split()))
        for j in s:
            l[j-1] += 1
    for i in range(n):
        if l[i] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
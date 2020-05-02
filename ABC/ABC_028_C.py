def main():
    ans = []
    l = list(map(int, input().split()))
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                ans.append(l[i] + l[j] + l[k])
    ans = list(set(ans))
    ans.sort(reverse=True)

    print(ans[2])

if __name__ == '__main__':
    main()
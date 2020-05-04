def main():
    ans = 0
    x = int(input())
    for i in range(-118,120):
        for j in range(-118, 120):
            if i**5 - j**5 == x:
                ans = [i,j]
                break 
    print(ans[0], ans[1])

if __name__ == '__main__':
    main()
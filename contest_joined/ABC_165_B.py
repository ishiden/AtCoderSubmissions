def main():
    ans = 0
    m = 100
    x = int(input())
    while m < x:
        m += m//100
        ans += 1 
    
    print(ans)

if __name__ == '__main__':
    main()
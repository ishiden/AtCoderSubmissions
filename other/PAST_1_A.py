def main():
    ans = 0
    try:
        n = int(input())
        ans = 2*n
    except:
        ans = 'error'
    print(ans)

if __name__ == '__main__':
    main()
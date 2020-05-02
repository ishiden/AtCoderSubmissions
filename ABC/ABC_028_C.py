def main():
    a,b,c,d,e = map(int, input().split())
    print(max(a+d+e, b+c+e))

if __name__ == '__main__':
    main()

"""
20200502 コンテスト中には解けず...
def main():
    n,m = map(int, input().split())
    ans = []
    if n % 2 != 0:
      n -= 1
      if m > 1:
            for i in range(m):
                ans.append([1+i, n-i])
            for i in ans:
                print(i[0], i[1])
        else:
            print(n//2, n//2+1)
    else:
        if m > 1:
            for i in range(m):
                ans.append([1+i, n-(i*2)])
            for i in ans:
                print(i[0], i[1])
        else:
            print(n//2, n//2+1)    

if __name__ == '__main__':
    main()
"""
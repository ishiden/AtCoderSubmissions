import collections as c
        
def main():
    n = int(input())
    a = 'indeednow'
    lena = len(a)
    ca = c.Counter(a)
    print(ca)
    for i in range(n):
        ans = 'YES'
        s = input()
        if len(s) != lena or ca != c.Counter(s):
            ans = 'NO'
        print(ans)

if __name__ == '__main__':
    main()
"""
20200502 コンテスト中には解けず...
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    ans = 0
    n,m,q = map(int, input().split())
    # l = []
    A = []
    r = combinations_count(m-1, n-1)
    for i in range(r):


    for i in range(q):
        a,b,c,d = map(int, input().split())

        # l.append(list(map(int, input().split())))
    
    
    print(ans)

if __name__ == '__main__':
    main()
"""
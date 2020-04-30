import numpy as np

def main():
    ans = 0
    n = int(input())
    m = list(map(int, input().split()))
    l = np.arange(1,n+1)
    lm = list(zip(l, m))
    lm.sort(key = lambda x: x[1], reverse=True)

    for i in range(n):
        print(lm[i][0])

if __name__ == '__main__':
    main()
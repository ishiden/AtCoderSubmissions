import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    h = list(map(int, input().split()))[::-1]
    for i in range(N-1):
        if h[i] < h[i+1]:
            if h[i+1]-h[i] > 1:
                ans='No'
                break
            else:
                h[i+1] -= 1

    print(ans)

if __name__ == '__main__':
    main()
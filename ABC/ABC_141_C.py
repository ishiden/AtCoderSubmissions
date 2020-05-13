import sys

input = sys.stdin.readline

def main():
    ans = ''
    N, K, Q = map(int, input().split())
    a = [K-Q]*N
    for _ in range(Q):
        a[int(input())-1] += 1
    for i in a:
        if i > 0:
          ans += 'Yes'
        else:
          ans += 'No'
        ans += '\n'
    print(ans)

if __name__ == '__main__':
    main()
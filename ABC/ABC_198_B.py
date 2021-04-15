import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    N = input().rstrip('\n')
    for i in range(11):
        n = '0' * i + N
        if n == n[::-1]:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    ans = ''
    odd = []
    even = []
    n = int(input())
    A = input().rstrip('\n').split(' ')
    for i in range(n):
        if i % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
    if n % 2 == 0:
        ans = ' '.join(odd) + ' ' + ' '.join(even)
    else:
        ans = ' '.join(even) + ' ' + ' '.join(odd)
    print(ans)

if __name__ == '__main__':
    main()
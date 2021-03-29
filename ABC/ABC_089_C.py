import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    l = [0] * 5
    s = 'MARCH'
    for i in range(N):
        f = input()[0]
        if f not in s:
            continue
        l[s.index(f)] += 1
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                ans += l[i] * l[j] * l[k]
    print(ans)

if __name__ == '__main__':
    main()
import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    l = []
    for _ in range(N):
        l.append(list(map(int, input().split())))
    s_l = sorted(l, key = lambda x:x[1])
    spent = 0
    for i in range(N):
        spent += s_l[i][0]
        if spent > s_l[i][1]:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()
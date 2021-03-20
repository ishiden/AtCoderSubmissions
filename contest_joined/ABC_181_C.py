import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    l = []
    for _ in range(N):
        x, y = map(int, input().split())
        l.append([x, y])
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (l[k][0]-l[i][0])*(l[j][1]-l[i][1]) == (l[j][0]-l[i][0])*(l[k][1]-l[i][1]):
                    ans = 'Yes'
                    print(ans)
                    exit()
    print(ans)

if __name__ == '__main__':
    main()
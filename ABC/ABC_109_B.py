import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    wl = []
    wl.append(input().rstrip('\n'))
    for i in range(1,N):
        wl.append(input().rstrip('\n'))
        if wl[i-1][-1] != wl[i][0]:
            ans = 'No'
            break
    if len(wl) != len(set(wl)):
        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()
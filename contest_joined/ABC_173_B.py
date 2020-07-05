import sys

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    ans = [0, 0, 0, 0]
    S = ['AC', 'WA', 'TLE', 'RE']
    for i in range(N):
        s = input().rstrip('\n')
        ans[S.index(s)] += 1
    print(f'AC x {ans[0]}')
    print(f'WA x {ans[1]}')
    print(f'TLE x {ans[2]}')
    print(f'RE x {ans[3]}')

if __name__ == '__main__':
    main()
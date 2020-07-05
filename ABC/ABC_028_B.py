import sys

input = sys.stdin.readline

def main():
    ans = [0,0,0,0,0,0]
    S = input().rstrip('\n')
    for i in S:
        if i == 'A':
            ans[0] += 1
        elif i == 'B':
            ans[1] += 1
        elif i == 'C':
            ans[2] += 1
        elif i == 'D':
            ans[3] += 1
        elif i == 'E':
            ans[4] += 1
        elif i == 'F':
            ans[5] += 1
    print(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5])

if __name__ == '__main__':
    main()

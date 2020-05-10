import sys

input = sys.stdin.readline

def main():
    t = 'ATGC'
    ans = 0
    S = input()
    temp = 0
    for s in S:
        if s in t:
            temp += 1
        else:
            ans = max(ans, temp)
            temp = 0

    print(ans)

if __name__ == '__main__':
    main()

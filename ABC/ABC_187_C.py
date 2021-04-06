import sys

input = sys.stdin.readline

def main():
    ans = 'satisfiable'
    N = int(input())
    l = set()
    for i in range(N):
        l.add(input().rstrip('\n'))
    for i in l:
        if i[0] == '!':
            if i[1:] in l:
                ans = i[1:]
                break
        else:
            if '!' + i in l:
                ans = i
                break
    print(ans)

if __name__ == '__main__':
    main()
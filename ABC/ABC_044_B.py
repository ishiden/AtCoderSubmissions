import sys

input = sys.stdin.readline

def main():
    ans = 'Yes'
    w = input().rstrip('\n')
    s = set(w)
    for i in s:
        if w.count(i)%2 != 0:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()

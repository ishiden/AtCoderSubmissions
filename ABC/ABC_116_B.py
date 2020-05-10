import sys

input = sys.stdin.readline

def calc(n):
    if n%2 == 0:
        return n//2
    else:
        return n*3 + 1

def main():
    ans = 1
    s = int(input())
    l = [s]
    while True:
        temp = calc(l[ans-1])
        ans += 1
        if temp in l:
            break
        else:
            l.append(temp)
    print(ans)

if __name__ == '__main__':
    main()
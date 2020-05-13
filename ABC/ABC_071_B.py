import sys
import string

input = sys.stdin.readline

def main():
    ans = 'None'
    S = input()
    s = string.ascii_lowercase
    for i in s:
        if i not in S:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()
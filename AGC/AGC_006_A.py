import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    s = input().rstrip('\n')
    t = input().rstrip('\n')
    for i in range(n):
        if s[i:] == t[:n-i]:
            print(n+i)
            break
    else:
        print(n*2)

if __name__ == '__main__':
    main()

# import sys

# input = sys.stdin.readline

# def checkSpell(s, t):
#     return s == t

# def main():
#     n = int(input())
#     s = input()
#     t = input()
#     for i in range(n):
#         ans = 0
#         for j in range(n):
#             if s[i] == t[j]:
#                 while checkSpell(s[i], t[j]):
#                     ans += 1
#                     i += 1
#                     j += 1
#                     if i == n or j == n:
#                         print(n*2 - ans)
#                         sys.exit()
#     print(n*2)

# if __name__ == '__main__':
#     main()
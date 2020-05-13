import sys

input = sys.stdin.readline

def main():
    n = int(input())
    i = 0
    while n > 0:
        i += 1
        n //= 2

    print(2**i - 1)

if __name__ == '__main__':
    main()

# 修正案：bit使うとコードが短くなる
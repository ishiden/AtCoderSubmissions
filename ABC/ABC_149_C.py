import sys
import math

input = sys.stdin.readline

def check(x):
    for n in range(2, int(math.sqrt(x)) + 1):
            if x % n == 0:
                return False
    return True

def main():
    ans = 0
    x = int(input())
    while check(x) == False:
        x += 1
    print(x)

if __name__ == '__main__':
    main()
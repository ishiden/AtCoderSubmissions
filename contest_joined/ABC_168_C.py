import sys
import math

input = sys.stdin.readline

def main():
    ans = 0
    A, B, H, M = map(int, input().split())
    h = 0.5*(H*60+M)
    m = 6*M
    d = abs(h-m)
    r = math.radians(d)
    ans = A**2 + B**2 - 2*A*B*math.cos(r)

    print('{:.20}'.format(ans**0.5))

if __name__ == '__main__':
    main()

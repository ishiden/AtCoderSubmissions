import sys

input = sys.stdin.readline

def main():
    ans = 0
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    for i in range(A+1):
        f = i*500
        if f == X:
            ans += 1
            break
        elif f > X:
            break
        for j in range(B+1):
            h = j*100
            if f + h == X:
                ans += 1
                break
            elif f + h > X:
                break
            for k in range(C+1):
                if f + h + k*50 == X:
                    ans += 1
                    break
    print(ans)

if __name__ == '__main__':
    main()

# break条件を繰り返し範囲の指定に組み込むことで処理速度向上できる
# min(x//500+1,a+1)
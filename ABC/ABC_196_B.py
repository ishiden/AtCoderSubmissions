import sys

input = sys.stdin.readline

def main():
    X = input()
    ans = X
    for i in range(len(X)):
        if X[i] == '.':
            ans = X[:i]
            break

    print(ans)

if __name__ == '__main__':
    main()
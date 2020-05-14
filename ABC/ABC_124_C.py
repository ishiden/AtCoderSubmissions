import sys

input = sys.stdin.readline

def main():
    S = input().rstrip('\n')
    l = len(S)
    ws = bs = ''
    for i in range(l):
        if i%2 == 0:
            ws += '0'
            bs += '1'
        else:
            ws += '1'
            bs += '0'
    wsc = bsc = 0
    for i in range(l):
        if S[i] != ws[i]:
            wsc += 1
        if S[i] != bs[i]:
            bsc += 1
    print(min(wsc, bsc))

if __name__ == '__main__':
    main()
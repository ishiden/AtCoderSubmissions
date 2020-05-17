import sys

input = sys.stdin.readline

def main():
    S = input().rstrip('\n')
    t = '0168'
    if S[-1] == '3':
        print('bon')
    elif S[-1] in t:
        print('pon')
    else:
        print('hon')
if __name__ == '__main__':
    main()
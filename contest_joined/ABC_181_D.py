import sys
from collections import Counter

input = sys.stdin.readline

def main():
    ans = 'No'
    S = input().rstrip('\n')
    cnt = Counter(S)
    if len(S) <= 2:
        if int(S)%8 == 0 or int(S[::-1])%8 == 0:
            ans = 'Yes'
    else:
        for i in range(13, 126):
            if not Counter(str(i*8)) - cnt:
                ans = 'Yes'
                break
    print(ans)

if __name__ == '__main__':
    main()

# 時間内に解けず。
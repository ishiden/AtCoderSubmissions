import sys
import math

input = sys.stdin.readline

def main():
    ans = 0
    e = 'o'
    q = '?'
    n = 'x'
    el, ql, nl = [], [], []

    S = list(input())
    for i in range(10):
        if S[i] == e:
            el.append(str(i))
        elif S[i] == q:
            ql.append(str(i))
        else:
            nl.append(str(i))

    if len(el) >= 5 or len(nl) == 10:
        ans = 0
    elif len(el) == 4:
        ans = 24
    else:
        for i in range(10):
            if str(i) in nl:
                continue
            for j in range(10):
                if str(j) in nl:
                    continue
                for k in range(10):
                    if str(k) in nl:
                        continue
                    for l in range(10):
                        if str(l) in nl:
                            continue
                        v = str(i) + str(j) + str(k) + str(l)
                        if all(s in v for s in el) and all(t not in v for t in nl):
                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
           lower_divisors.append(i)
           if i != n // i:
               upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    ans = 0
    K = int(input())
    #Kの約数を昇順に列挙
    d = make_divisors(K)
    l = len(d)
    #約数リストを重複ありで２重ループ
    for i in range(l):
        for j in range(i, l):
            tmp = d[i] * d[j]
            #2つの約数の積がKを超えた場合は、以降条件を満たさないためスキップ
            if tmp > K:
                break
            #2つの約数の積でKを割った商が2つ目の約数より小さい場合は、計上済みのため以降スキップ
            if K//tmp < d[j]:
                break
            #2つの約数の積でKが割り切れたら計上
            if K%tmp == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
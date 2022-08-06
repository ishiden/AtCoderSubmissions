import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

#方針 辞書つかって尺取ちっくに
def main():
    ans = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #今見ている区間の各文字の登場回数
    d = collections.defaultdict(lambda: 0)
    #最初のK文字(区間)は絶対にK種類以下のため辞書につめる
    for i in range(K):
        d[A[i]] += 1
    #区間にある文字の種類数
    temp = len(d)
    #今見ている区間の文字数
    temp_ans = K
    #今見ている区間の始点
    s = 0
    for i in range(K, N):
        #既に今見ている区間に含まれている場合
        if d[A[i]] > 0:
            temp_ans += 1
        #含まれていない場合
        else:
            #区間の文字種類数がK未満なら文字数と種類数をプラス１
            if temp < K:
                temp_ans += 1
                temp += 1
            #区間の文字種類数がすでにKの場合
            else:
                #新しい文字を追加するために、区間の文字種類が１個へるまで始点をずらす
                for j in range(s, i):
                    d[A[j]] -= 1
                    if d[A[j]] == 0:
                        s = j+1
                        break
                    else:
                        temp_ans -= 1
        #今見ている文字を辞書でカウントアップ
        d[A[i]] += 1
        #最大値更新
        ans = max(temp_ans, ans)

    print(ans)

if __name__ == '__main__':
    main()
import itertools

ans = 0
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
for i,j,k,l,m in itertools.combinations(A, 5):
    if i*j%P*k%P*l%P*m%P == Q:
        ans += 1
print(ans)
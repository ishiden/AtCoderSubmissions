d,n = map(int,input().split())
ans = 0
if n != 100:
  ans = 100**d * n
else:
  ans = 100**d * 101
print(ans)

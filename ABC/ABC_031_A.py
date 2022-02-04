ans = 0
a, b = map(int, input().split())
if a > b:
  ans = a * (b + 1)
else:
  ans = (a + 1) * b
print(ans)
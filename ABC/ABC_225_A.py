s = list(input())
sets = set(s)
ans = 6
l = len(sets)
if l == 2:
  ans = 3
elif l == 1:
  ans = 1
print(ans)

import itertools

n = int(input())
l = itertools.product('abc', repeat=n)
for s in l:
  print(''.join(s))
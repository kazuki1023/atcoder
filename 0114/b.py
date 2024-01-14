n = int(input())
a = []
if n % 1 == 1:
  print(0)
else:
  while True:
    q, r = n //2, n % 2
    a.append(r)
    n = q
    if q <= 0:
      break
print(a.index(1))



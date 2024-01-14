n = int(input()) -1
b = []
while True:
  q, r = n // 5, n % 5
  b.append(r)
  n = q
  if q <= 0:
    break
g = [0,2,4,6,8]
s = 0
for index, value in enumerate(b):
  if index == 0:
    s += g[value]
  else:
    s += (10**index)*g[value]
print(s)

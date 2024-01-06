n ,d = map(int, input().split())
t = list(map(int, input().split()))
result = ''
for i in range(n-1):
  if t[i+1] - t[i] > d:
    continue
  elif t[i+1] - t[i] <= d:
    result  = t[i + 1]
    break
if(result == ''):
  print(-1)
else:
  print(result)

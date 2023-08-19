m = int(input())
d = list(map(int,input().split()))
sum = sum(d)
middle = sum // 2 + 1
test = 0
p = 0
month = 0
for i in range(m):
  if(test < middle):
    test += d[i]
    month = i + 1
  else:
    test -= d[i - 1]
    month = i
    break
if test == middle:
  print(month, middle)
else:
  print(month, middle-test)
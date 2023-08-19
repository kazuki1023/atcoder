n = int(input())
num_list = []
p_list = []
for i in range(n):
    p_list.append(list(map(int,input().split())))
    num_list.append(list(map(int,input().split())))
x = int(input())
a = []
for i in range(n):
    if x in num_list[i]:
      a.append(i)
if len(a) == 0:
  print(0)
else:
  result = []
  for j in a:
    result.append(p_list[j])
  k = ([p for p, v in list(enumerate(result)) if v == min(result)])
  answer = []
  for i in k:
    answer.append(a[i] + 1)
  print(len(k))
  print(*answer)
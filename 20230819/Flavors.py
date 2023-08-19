n = int(input())
l = [list(map(int, input().split())) for l in range(n)]
value = max(list(map(lambda x: max(x), l)))
test = sorted(list(map(lambda x: max(x), l)) , reverse=True)
print(test)
for i in range(n):
  if l[i][1] == value:
    print(i + 1, l[i][0], value)
  if l[i][1] == test[1]:
    print(i + 1, l[i][0], test[1])
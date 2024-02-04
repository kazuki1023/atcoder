n = int(input())
t = [[] for _ in range(n)]
for i in range(n):
  s = list(map(str, input().split()))
  t[i] = s
print(t)

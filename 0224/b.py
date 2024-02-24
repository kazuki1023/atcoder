n = int(input())
p = list(map(int, input().split()))
q = int(input())
s = [list(map(int, input().split())) for l in range(q)]
for i in range(q):
  a = p.index(s[i][0])
  b = p.index(s[i][1])
  if a > b:
    print(s[i][1])
  else:
    print(s[i][0])

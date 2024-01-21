n = int(input())
l = [list(map(int, input().split())) for l in range(n)]
a = 0
b = 0
for i in l:
  a += i[0]
  b += i[1]
if a > b:
  print("Takahashi")
elif a < b:
  print("Aoki")
else:
  print("Draw")

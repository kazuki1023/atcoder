n,m = map(int, input().split())
num_list = []
for i in range(m):
    num_list.append(list(map(int,input().split())))
# N人分のリストを作成
p = [0]*n
for item in num_list:
    q = int(item[0])
    t = int(item[1])
    p[q - 1] += 1
    p[t - 1] -= 1
print(p)
s = max(p)
if m == 0:
    print(-1)
else:
      if(p.count(s) > 1):
        print(-1)
      else:
        print(p.index(s) + 1)
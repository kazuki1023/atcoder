n, p, q = map(int, input().split())
d_list = list(map(int, input().split()))

# 追加注文の最小値を求める
d_min = min(d_list)

if (p <= q + d_min):
    print(p)
else:
  print(q + d_min)

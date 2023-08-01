N = int(input())
A = list(map(int, input().split()))
cnt = [0]*N
r = 0
for index, i in enumerate(A):
  # 2で何回割れるか調べる
  while i%2 == 0 and r == 0:
    i, r = divmod(i, 2)
    cnt[index] += 1
print(min(cnt))
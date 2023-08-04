n = int(input())
a = list(map(int, input().split()))
# 各週の合計値を求める
# 歩数データを7日単位に分割
chunks = [a[i:i + 7] for i in range(0, len(a), 7)]

# 各週間の歩数合計を計算
result = [sum(chunk) for chunk in chunks]

print(*result)


# n = int(input())
# l = list(map(int,input().split()))
# a = list()

# for i in range(n):
#   total = sum(l[i*7:i*7+7])
#   a.append(total)

# print(*a)
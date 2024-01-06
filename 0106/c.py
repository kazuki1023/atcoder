# n, q = map(int, input().split())
# a = [[i + 1, 0] for i in range(n)]
# result = []
# for _ in range(q):
#     query = input().split()
#     if query[0] == '1':
#         action = query[1]
#         head = a[0].copy()
#         if action == 'U':
#             a[0][1] += 1
#         elif action == 'D':
#             a[0][1] -= 1
#         elif action == 'L':
#             a[0][0] -= 1
#         elif action == 'R':
#             a[0][0] += 1
#         for i in range(1, n):
#             a[i], prev_head = prev_head, a[i]
#     if query[0] == '2':
#         action = int(query[1]) - 1
#         result.append(a[action])
# print(result)

n, q = map(int, input().split())
a = [[i + 1, 0] for i in range(n)]
result = []

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        action = query[1]
        # 頭の現在の位置をコピー
        head = a[0].copy()
        if action == 'U':
            a[0][1] += 1
        elif action == 'D':
            a[0][1] -= 1
        elif action == 'L':
            a[0][0] -= 1
        elif action == 'R':
            a[0][0] += 1

        # 他のパーツを更新
        for i in range(1, n):
            a[i], head = head, a[i]

    elif query[0] == '2':
        p = int(query[1]) - 1
        result.append(a[p])

# 結果の出力
for res in result:
    print(*res)


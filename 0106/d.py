N = int(input())
box = [[0] * N for _ in range(N)]

x, y = 0, 0
dx, dy = 0, 1
count = 1

while True:
    box[x][y] = count
    if count == N * N:
        break
    count += 1

    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= N or ny < 0 or ny >= N or box[nx][ny] != 0:
        dx, dy = dy, -dx

    x, y = x + dx, y + dy

box[N // 2][N // 2] = 'T'

# 結果を出力
for row in box:
    print(" ".join(map(str, row)))

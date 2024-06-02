N, M = map(int, input().split())
A = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

all_passed = True  # フラグを設定

for j in range(M):
    a = 0
    for i in range(N):
        a += matrix[i][j]
    if a >= A[j]:
        continue  # 次の列に進む
    else:
        print("No")
        all_passed = False  # フラグを変更
        break

if all_passed:
    print("Yes")

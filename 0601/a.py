N, L, R= map(int, input().split())
list = [i + 1 for i in range(N)]
selected = list[L-1:R]
result = list[:L-1] + selected[::-1] + list[R:]
print(" ".join(map(str, result)))

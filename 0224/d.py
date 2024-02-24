import math
N = int(input())
A = list(map(int, input().split()))
square_indices = []

for i, a in enumerate(A):
    if a >= 0 and math.isqrt(a) ** 2 == a:
        square_indices.append(i)

count = 0
for i in range(len(square_indices)):
    for j in range(i + 1, len(square_indices)):
            count += 1
print(count)
